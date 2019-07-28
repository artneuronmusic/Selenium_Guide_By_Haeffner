
import unittest
from selenium import webdriver




class TestHovers(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):

        self.driver.quit()

    def test_example_1(self):
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com/javascript_alerts")
        driver.find_elements_by_tag_name("button")[0].click()
        popup = driver.switch_to.alert
        popup.accept()
        #popup.dismiss()
        result = driver.find_element_by_id("result").text
        assert result == "You successfully clicked an alert"

if __name__ == "__main__":
    unittest.main()




