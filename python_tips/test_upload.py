import os
import unittest

from selenium import webdriver
import time


class Upload(unittest.TestCase):

#setUp and tearDown will execute before each test in this class.

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        time.sleep(10)
        self.driver.quit()

    def test_example_1(self):
        driver = self.driver
        filename = "some-file.txt"
        file = os.path.join(os.getcwd(), filename)
        driver.get("http://the-internet.herokuapp.com/upload")
        driver.find_element_by_id('file-upload').send_keys(file)
        driver.find_element_by_id('file-submit').click()

        uploaded_file = driver.find_element_by_id('uploaded-files').text
        assert uploaded_file == filename #, "uploaded file should be {}".format(filename)

if __name__ == "__main__":
    unittest.main()




