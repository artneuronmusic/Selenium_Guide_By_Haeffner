from selenium.webdriver.common.by import By
from base_page import BasePage


class DynamicLoading(BasePage):

    _Example1 = {"by": By.LINK_TEXT, "value": "Example 1: Element on page that is hidden"}
    _Example2 = {"by": By.LINK_TEXT, "value": "Element 2: Element rendered after the fact"}
    _ExampleStart1 = {"by": By.CSS_SELECTOR, "value": "#start button"}
    _ExampleStart2 = {"by": By.CSS_SELECTOR, "value": "#start button"}
    _ExampleHello1 = {"by": By.ID, "value": "finish"}
    _ExampleHello2 = {"by": By.ID, "value": "finish"}



    def __init__(self,driver):
        self.driver = driver



    def dynamic_example_page(self, example_number):
        self._visit("/dynamic_loading/" + example_number)
        self._click(self._ExampleStart1)

    def finish_example1_present(self):
        return self._wait_for_is_displayed(self._ExampleHello1, 10)



