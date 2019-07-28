from selenium import webdriver
import unittest

class AbTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_forge_cookie_url(self):
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com/abtest?optimizely_opt_out=true")
        driver.switch_to.alert.dismiss() #this approach triggers a javascript alert, so solving the problem by switching and dimsmming it
        heading_text = driver.find_element_by_tag_name("h3").text
        assert heading_text == "No A/B Test"




#here is the thing: i still dont know whats this for... take udacity class, do project.





"""        
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com")
        driver.add_cookie({'name': 'optimizelyOptOut', 'value': 'true'})
        driver.get("http://the-internet.herokuapp.com/abtest")
        heading_text = driver.find_element_by_tag_name("h3").text
        assert heading_text == "No A/B Test"

"""

"""
    def test_forge_cookie(self):
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com/abtest")
        heading_text = driver.find_element_by_tag_name("h3").text
        assert heading_text in ['A/B Test Variation 1', 'A/B Test Control']

        driver.add_cookie({'name': 'optimizelyOptOut', 'value': 'true'})
        driver.refresh()
        heading_text = driver.find_element_by_tag_name("h3").text
        assert heading_text == "No A/B Test"
"""