from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_project_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//a[@href="/mantisbt-1.2.20/manage_overview_page.php"]').click()
        wd.find_element_by_xpath('//a[@href="/mantisbt-1.2.20/manage_proj_page.php"]').click()

    def create_project(self, project):
        wd = self.app.wd
        self.open_project_page()
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        self.fill_project_form(project)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
        self.open_project_page()
        self.project_cache = None

    def fill_project_form(self, project):
        self.change_field_value("name", project.name)
        self.change_field_value("status", project.status)
        self.change_field_value("view_state", project.view_state)
        self.change_field_value("description", project.description)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def open_project_page_by_id(self, id):
        wd = self.app.wd
        self.open_project_page()
        wd.find_element_by_xpath("//a[contains(@href, 'manage_proj_edit_page.php?project_id=%s')]" % id).click()

    def delete_project_by_id(self, id):
        wd = self.app.wd
        self.open_project_page_by_id(id)
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//div[contains(@text, '')]")
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        self.open_project_page()
        self.project_cache = None

    project_cache = None

