from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from driver.Client import AndroidClient, WebClient


class ChatPage(object):
    def __init__(self):
        self.android_driver = AndroidClient.restart_app()
        self.driver = self.android_driver
        self._textItem = (By.XPATH, '//android.widget.TextView[@resource-id="com.ss.android.lark:id/textItem" '
                                    'and @text="通讯录"]')
        self._tv_item = (By.XPATH, '//android.widget.TextView[@resource-id="com.ss.android.lark:id/tv_item" '
                                   'and @text="外部联系人"]')
        # self._contact_name = (By.XPATH, '//android.widget.TextView[@resource-id="com.ss.android.lark:id/contact_name" '
        #                                 'and @text="name"]')
        self._text = (By.XPATH, '//android.widget.TextView[@text="消息"]')
        self._kb_rich_text_content = (By.ID, 'com.ss.android.lark:id/kb_rich_text_content')
        self._btn_send = (By.XPATH, '//android.widget.ImageView[@resource-id="com.ss.android.lark:id/btn_send"]')

    def chat(self, name, keywords):
        _contact_name = (By.XPATH, '//android.widget.TextView[@resource-id="com.ss.android.lark:id/contact_name" '
                                   'and @text="%s"]' % name)
        self.driver.find_element(*self._textItem).click()
        self.driver.find_element(*self._tv_item).click()
        self.driver.find_element(*_contact_name).click()
        self.driver.find_element(*self._text).click()
        self.driver.find_element(*self._kb_rich_text_content).send_keys(keywords)
        self.driver.find_element(*self._btn_send).click()
        self.driver.implicitly_wait(10)
        self.driver.terminate_app('com.ss.android.lark')


class WebChatPage(object):
    def __init__(self):
        self.android_driver = WebClient.restart_app()
        self.driver = self.android_driver
        self._tip_contacts = (By.XPATH, "//section[@data-tip='tip-contacts']")

        self._message_input = (By.XPATH, "//input[@class='larkc-usercard__footer__input "
                                         "larkc-usercard__footer__message-input']")
        self._navbarMenu_active = (By.XPATH, "//section[@class='navbarMenu navbarMenu_active']")

    def webchat(self, contacts_name, contacts_message):
        _contacts_name = (By.XPATH, '//span[text()="%s"]' % contacts_name)

        self.driver.find_element(*self._tip_contacts).click()
        self.driver.find_element(*self._navbarMenu_active).click()
        self.driver.find_element(*_contacts_name).click()
        self.driver.find_element(*self._message_input).send_keys(contacts_message)
        ActionChains(self.driver).key_down(Keys.ENTER).perform()
        self.driver.implicitly_wait(10)
        self.driver.quit()


# wep = WebChatPage()
# wep.webchat(contacts_name='蔡志峰', contacts_message='Hellow World')
