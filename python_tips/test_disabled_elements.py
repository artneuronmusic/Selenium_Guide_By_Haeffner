import unittest
from selenium import webdriver
import time

class DisabledElements(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):

        self.driver.quit()

    def test_disabled(self):
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com/dropdown")
        dropdown_list = driver.find_elements_by_tag_name("option")
        time.sleep(3)
        assert dropdown_list[2].is_enabled() #dropdown_list[0] => please select an option

if __name__ == "__main__":
    unittest.main()