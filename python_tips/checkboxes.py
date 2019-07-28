import unittest
from selenium import webdriver
import time

class Checkboxes(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()


    def test_live_values(self):
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com/checkboxes")
        checkboxes = driver.find_elements_by_css_selector("input[type='checkbox']")

        print("\nWith .get_attribute('checked')")

        for i in checkboxes:
            print(i.get_attribute('checked'))
        assert checkboxes[-1].get_attribute('checked')
        # for i in range(0, len(checkboxes)):
            #print(checkboxes[i].get_attribute('checked'))
        time.sleep(2)

        print("\nWith .is_selected")

        for i in checkboxes:
            print(i.is_selected())
        assert checkboxes[0].is_selected()
        time.sleep(2)

        #for x in range(0, len(checkboxes)):
            #print(checkboxes[i].is_selected())

if __name__ == "__main__":
    unittest.main()

