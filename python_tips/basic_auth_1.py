import unittest
from selenium import webdriver

class BasicAuth1(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):

        self.driver.quit()

    def test_visit_auth_page(self):
        driver = self.driver
        driver.get("http://admin:admin@the-internet.herokuapp.com/basic_auth")
        #https://user:password@
        #message = driver.find_element_by_xpath("//div[@class='example']/p").text
        message = driver.find_element_by_css_selector("div.example p").text
        assert message == "Congratulations! You must have the proper credentials."

if __name__ == "__main__":
    unittest.main()
