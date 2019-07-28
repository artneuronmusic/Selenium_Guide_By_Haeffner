

#import sys
import unittest
from selenium import webdriver
import time



class ScreenShotOnFailure(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.save_screenshot("new_screen1.png")
        self.driver.quit()
        #if sys.exc_info()[0]: #handling an exception, For any stack frame, only information about the most recently handled exception is accessible.save the name of the error and the traceback details into a variable
            #test_method_name = self._testMethodName
         #   self.driver.save_screenshot_as_file("Screenshots/%s.png" % self._testＭethodName)
        #

        self.driver.quit()


    def test_example_1(self):
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com")
        #assert driver.title == "NOOOOOOOO"
        time.sleep(3)


if __name__ == "__main__":
    unittest.main()
