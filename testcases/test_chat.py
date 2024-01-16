import pytest
from driver.AndroidClient import AndroidClient
from page.ChatPage import ChatPage, WebChatPage


class TestChat(object):
    def test_chat(self):
        self.test_chat = ChatPage()
        self.test_chat.chat('your_name', 'hello word')


class TestWebChat(object):
    def test_webchat(self):
        self.test_webchat = WebChatPage()
        self.test_webchat.webchat('your_name', 'Hellow Word')


if __name__ == '__main__':
    pytest.main(['test_chat.py'])

