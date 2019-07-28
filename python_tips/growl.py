import unittest
from selenium import webdriver
import time


class TestFrames(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_example_1(self):
        driver = self.driver
        driver.execute_scipt(
            "if (!window.jQuery) {"
            "var jquery = document.createElement('script');"
            "jquery.type = 'text/javascript';"
            "jquery.src = "
        })
