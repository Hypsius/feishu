import time
from time import sleep
from appium.webdriver import webdriver
from appium import webdriver
from selenium.webdriver.common.by import By
from driver.Client import AndroidClient


class LoginPage(object):
    def __init__(self, driver: webdriver):
        self.driver = driver
        self._ud_dialog_btn_primary = (By.ID, "com.ss.android.lark:id/ud_dialog_btn_primary")
        self._startLoginBtn = (By.ID, "com.ss.android.lark:id/startLoginBtn")
        self._phone_number_edit = (By.ID, "com.ss.android.lark:id/phone_number_edit")
        self._btn_next = (By.ID, "com.ss.android.lark:id/btn_next")
        self._signin_sdk_input_pass_word_edit_text = (
            By.ID, "com.ss.android.lark:id/signin_sdk_input_pass_word_edit_text")
        self._signin_sdk_widget_footer_btn = (By.ID, "com.ss.android.lark:id/signin_sdk_widget_footer_btn")

    def loginByPassword(self, phone_number, password):
        self.driver.find_element(*self._ud_dialog_btn_primary).click()
        self.driver.find_element(*self._startLoginBtn).click()
        self.driver.find_element(*self._phone_number_edit).send_keys(phone_number)
        self.driver.find_element(*self._btn_next).click()
        self.driver.find_element(*self._ud_dialog_btn_primary).click()
        self.driver.find_element(*self._signin_sdk_input_pass_word_edit_text).send_keys(password)
        self.driver.find_element(*self._signin_sdk_widget_footer_btn).click()

    # def terminate_app(self):
    #     time.sleep(10)
    #     self.driver.terminate_app('com.ss.android.lark')  # 退出app

# android_driver = AndroidClient.install_app()
# new_page = LoginPage(driver=android_driver)
# new_page.loginByPassword(phone_number='13430116165', password='tester-001')


class WebLogin(object):
    def __init__(self, driver: webdriver):
        self.driver = driver
        self._switch_icon = (By.XPATH, "//span[@class='universe-icon switch-icon']")
        self._mobile_input = (By.NAME, 'mobile_input')
        self._next_btn = (By.XPATH, "//button[text()='下一步']")
        self._approve_btn = (By.XPATH, "//button[text()='同意']")
        self._password = (By.XPATH, "//input[@type='password']")
        self._login_btn = (By.XPATH, "//button[contains(@data-test,'login-pwd-next-btn')]")

    def loginByPassword(self, mobile, password):
        self.driver.find_element(*self._switch_icon).click()
        self.driver.find_element(*self._mobile_input).send_keys(mobile)
        self.driver.find_element(*self._next_btn).click()
        self.driver.find_element(*self._approve_btn).click()
        self.driver.find_element(*self._password).send_keys(password)
        self.driver.find_element(*self._login_btn).click()
        #   最后一步需要输入验证码，解决办法：1.手动输入验证码  2.使用短信转发器，监听端口API请求获取输入验证码


