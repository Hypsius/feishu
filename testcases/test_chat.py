import pytest

from driver.Client import AndroidClient
from page.ChatPage import ChatPage, WebChatPage


class TestChat(object):
    def test_chat(self):
        self.test_chat = ChatPage()
        self.test_chat.chat('蔡志峰', 'hello word1')


# class TestWebChat(object):
#     def test_webchat(self):
#         self.test_webchat = WebChatPage()
#         self.test_webchat.webchat('蔡志峰', 'Hellow Word2')


if __name__ == '__main__':
    pytest.main(['test_chat.py'])

