import unittest
from selenium import webdriver

import time

class TestDropDown(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):

        self.driver.quit()

    def test_example_drop_down(self):
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com/dropdown")
        option = driver.find_elements_by_tag_name("option")

        for i in option:
            if i.text == "Option 1":
                i.click()
                break

        for x in option:

            if x.is_selected():
                selected_option = x.text
                break
        assert selected_option == "Option 1"

if __name__ == "__main__":
    unittest.main()





