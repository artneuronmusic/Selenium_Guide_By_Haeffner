import pytest

from login_page import LoginPage


class TestLogin():


    @pytest.fixture
    def login(self, driver):
        return LoginPage(driver)

    def test_valid_credentials(self, login):

        login.login_detail("tomsmith", "SuperSecretPassword!")
        assert login.login_presentation()

    def test_invalid_credentials(self, login):
        login.login_detail("tomsmit", "SuperSecretPassword!")
        assert login.login_presentation() == False









