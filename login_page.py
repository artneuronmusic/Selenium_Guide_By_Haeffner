from selenium.webdriver.common.by import By
from FireFox_project.Pages.base_page import BasePage
import time

class LoginPage(BasePage):
    _loginName = {"by": By.NAME, "value": "username"}
    _loginPassword = {"by": By.NAME, "value": "password"}
    _loginSubmit = {"by": By.CLASS_NAME, "value": "radius"}
    _loginSuccess = {"by": By.CSS_SELECTOR, "value": ".flash.success"}
    _loginFailure = {"by": By.CSS_SELECTOR, "value": ".flash.error"}
    _loginContent = {"by": By.CLASS_NAME, "value": "subheader"}

    def __init__(self, driver):
        self.driver = driver
        # self._visit("http://the-internet.herokuapp.com/login")
        self._visit("/login")
        assert self._is_displayed(self._loginContent)




    def login_detail(self, username, password):

        self._type(self._loginName, username)
        self._type(self._loginPassword, password)
        self._click(self._loginSubmit)
        time.sleep(3)
        print(self.driver.title)

    def login_presentation(self):
        return self._is_displayed(self._loginSuccess)

    def login_invalid_presentation(self):
        return self._is_displayed(self._loginFailure)

    def success_message_present(self):
        self._wait_for_is_displayed(self._loginSuccess, 1)
        assert self._is_displayed(self._loginSuccess)


    def failure_message_present(self):
        self._wait_for_is_displayed(self._loginFailure, 1)
        assert self._is_displayed(self._loginFailure)


