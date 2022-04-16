import json
import pytest
import os.path
import importlib

from fixture.application import Application

fixture = None
target = None


def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
    return target


@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    web_config = load_config(request.config.getoption("--target"))['web']
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, baseURL=web_config['baseURL'])
    return fixture


@pytest.fixture(scope='session', autouse=True)
def stop(request):
    def finalizer():
        fixture.destroy()

    request.addfinalizer(finalizer)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--target", action="store", default="target.json")
    parser.addoption("--browser", action="store", default="firefox")


def load_from_module(module):
    return importlib.import_module("data.%s" % module).testdata
