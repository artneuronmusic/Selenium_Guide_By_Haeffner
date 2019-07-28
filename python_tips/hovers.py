
import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains



class TestHovers(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):

        self.driver.quit()

    def test_example1(self):
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com/hovers")
        avatar = driver.find_element_by_class_name("figure")
        ActionChains(driver).move_to_element(avatar).perform()
        avatar_caption = driver.find_element_by_class_name('figcaption')
        assert avatar_caption.is_displayed()

if __name__ == "__main__":
    unittest.main()

