import unittest
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.action_chains import ActionChains


class TestHovers(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):

        self.driver.quit()

    def test_example_1(self):
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com/windows")
        window_before = driver.window_handles[0]
        driver.find_element_by_partial_link_text("Click Here").click()
        window_after = driver.window_handles[1]
        driver.switch_to(window_after)
