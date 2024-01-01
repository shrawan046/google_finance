import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture()
def setup(browser):
    options = Options()
    options.add_argument('--headless=new')
    if browser == 'chrome':
        driver = webdriver.Chrome(options=options)
        print("Launching Chrome Browser")
    elif browser == 'firefox':
        driver = webdriver.Firefox(options=options)
        print("Launching Chrome Browser")
    else:
        driver = webdriver.Chrome(options=options)
        print("Launching default Browser")
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver


"""""
@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome Browser")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Chrome Browser")
    else:
        driver = webdriver.Chrome()
        print("Launching default Browser")
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver    """""


def pytest_addoption(parser):
    parser.addoption("--browser")
    # parser.addoption("--headless", action="store", default="headless", help="Is headless driver?")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


def pytest_configure(config):
    config._metadata = {
        "Tester": "Shrawan",
        "Project Name": "Google Finance Automation",
    }


@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
