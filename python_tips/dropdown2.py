import unittest
from selenium import webdriver
from selenium.webdriver.support.select import Select as WebDriverSelect



class TestDropDown(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):

        self.driver.quit()

    def test_example_drop_down(self):
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com/dropdown")
        option = driver.find_element_by_id("dropdown")

        select_list = WebDriverSelect(option)
        select_list.select_by_visible_text('Option 2')
        selection_option = select_list.first_selected_option.text
        #all_selected_options
        #deselect_all()
        #deselect_by_visible_text
        assert selection_option == "Option 2"


if __name__ == "__main__":
    unittest.main()