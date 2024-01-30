import pytest
from driver.AndroidClient import AndroidClient
from driver.WebClient import WebClient
from page.LoginPage import LoginPage, WebLogin


class TestLogin(object):
    @classmethod
    def setup_class(cls):
        cls.android_driver = AndroidClient.install_app()

    def test_login(self):
        main_page = LoginPage(driver=self.android_driver)
        main_page.loginByPassword(phone_number='phone', password='tester-001')
        main_page.getErrorMsg()


class TestWebLogin(object):
    @classmethod
    def setup_class(cls):
        cls.android_driver = WebClient.install_app()

    def test_login(self):
        main_page = WebLogin(driver=self.android_driver)
        main_page.loginByPassword(mobile='phone', password='tester-002')
        main_page.getErrorMsg()


if __name__ == '__main__':
    pytest.main(['test_login.py'])


