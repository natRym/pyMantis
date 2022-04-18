from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from fixture.session import SessionHelper
from fixture.james import JamesHelper



class Application:

    def __init__(self, browser, config):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "edge":
            self.wd = webdriver.Edge()
        else:
            raise ValueError("unrecognized browser %s" % browser)
        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.james = JamesHelper(self)
        self.config = config
        self.baseURL = config['web']['baseURL']

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.baseURL)

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def destroy(self):
        self.wd.quit()
