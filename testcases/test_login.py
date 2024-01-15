import pytest
from driver.Client import AndroidClient, WebClient
from page.LoginPage import LoginPage, WebLogin


class TestLogin(object):
    @classmethod
    def setup_class(cls):
        cls.android_driver = AndroidClient.install_app()

    def test_login(self):
        main_page = LoginPage(driver=self.android_driver)
        main_page.loginByPassword(phone_number='13430116165', password='tester-001')


# class TestWebLogin(object):
#     @classmethod
#     def setup_class(cls):
#         cls.android_driver = WebClient.install_app()
#
#     def test_login(self):
#         main_page = WebLogin(driver=self.android_driver)
#         main_page.loginByPassword(mobile='13316090732', password='tester-002')


if __name__ == '__main__':
    pytest.main(['test_login.py'])


