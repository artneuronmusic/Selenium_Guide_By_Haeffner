import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname("__file__"), "..", ".."))
from FireFox_project.Tests import config
from selenium import webdriver



def pytest_addoption(parser):
    parser.addoption("--baseurl",
                     action="store",
                     default="http://the-internet.herokuapp.com",
                     help="base URL for the application under test")

    parser.addoption("--browser",
                     action="store",
                     default="firefox",
                     help="the name of the browser you want to test with")


@pytest.fixture
def driver(request):
    config.baseurl = request.config.getoption("--baseurl")
    config.browser = request.config.getoption("--browser").lower()

    if config.browser == "firefox":
        driver_ = webdriver.Firefox(executable_path="/Users/yuchienhuang/Desktop/python_selenium/FireFox_project/vendors/geckodriver")

    elif config.browser == "chrome":
        driver_ = webdriver.Chrome(executable_path="/Users/yuchienhuang/Desktop/python_selenium/FireFox_project/vendors/chromedriver")




    def quit():
        driver_.quit()

    request.addfinalizer(quit)
    return driver_

