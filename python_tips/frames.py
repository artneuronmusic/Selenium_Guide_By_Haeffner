import unittest
from selenium import webdriver
import time


class TestFrames(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):

        self.driver.quit()

    def test_example_1(self):
        driver=self.driver
        driver.get("http://the-internet.herokuapp.com/tinymce")
        whole_frame = driver.find_element_by_id("mce_0_ifr")
        driver.switch_to.frame(whole_frame)
        editor = driver.find_element_by_id("tinymce")
        before_text = editor.text
        editor.clear()
        editor.send_keys("Hello~~~~~~~~~~")
        after_text = editor.text
        time.sleep(5)
        assert after_text != before_text

        driver.switch_to.default_content() #jump back to the top level of the page
        assert driver.find_element_by_css_selector("h3").text != " "


if __name__ == "__main__":
    unittest.main()