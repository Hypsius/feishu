import pytest
from page.ChatPage import ChatPage, WebChatPage


class TestChat(object):
    def test_chat(self):
        self.test_chat = ChatPage()
        self.test_chat.chat('your_name', 'hello word')
        #  已在ChatPage函数中断言


class TestWebChat(object):
    def test_webchat(self):
        self.test_webchat = WebChatPage()
        self.test_webchat.webchat('your_name', 'Hellow Word')
        #  已在ChatPage函数中断言


if __name__ == '__main__':
    pytest.main(['test_chat.py'])

