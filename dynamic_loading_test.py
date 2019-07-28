import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from dynamic_loading_page import DynamicLoading
import time





class TestDynamicLoading():

    @pytest.fixture
    def driver(self, request):

        driver_ = webdriver.Firefox()

        def quit():
            driver_.quit()

        request.addfinalizer(quit)
        #return DynamicLoading(driver_)
        return DynamicLoading(driver_)


    def test_dynamic_example1(self, driver):
        driver.dynamic_example_page("1")
        assert driver.finish_example1_present()


    def test_dynamic_element2(self, driver):
        driver.dynamic_example_page("2")
        assert driver.finish_example1_present()



        #time.sleep(3)



"""    
        #time.sleep(3)
      
        driver.find_element(By.LINK_TEXT, 'Example 1: Element on page that is hidden').click()
        driver.find_element(By.CSS_SELECTOR, "#start button").click()
        time.sleep(8)
        assert driver.find_element(By.ID, "finish").is_displayed()
        


    def test_dynamic_exmaple2(self, driver):
        driver.get("http://the-internet.herokuapp.com/dynamic_loading")
        time.sleep(3)
        driver.find_element(By.LINK_TEXT, 'Example 2: Element rendered after the fact').click()
        driver.find_element(By.CSS_SELECTOR, "#start button").click()
        time.sleep(8)
        assert driver.find_element(By.ID, "finish").is_displayed()


"""



