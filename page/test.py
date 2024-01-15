import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

# class WebClient(object):
#     @classmethod
#     def webclient(cls):
options = webdriver.ChromeOptions()
# # 使用已经登录过的chrome浏览器实例，实现cookie免登录
options.add_argument('--user-data-dir=C:/Users/gientech/AppData/Local/Google/Chrome/User Data/Profile 3')
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://m1py807zvq8.feishu.cn/messenger/")
driver.implicitly_wait(10)

try:
    element = driver.find_element(By.XPATH, "//span[text()='收件箱']")
    print('成功登录')

except NoSuchElementException:
    print()
    driver.find_element(By.XPATH, "//span[@class='universe-icon switch-icon']").click()
    driver.find_element(By.NAME, 'mobile_input').send_keys("13316090732")
    driver.find_element(By.XPATH, "//button[text()='下一步']").click()
    driver.find_element(By.XPATH, "//button[text()='同意']").click()
    driver.find_element(By.XPATH, "//input[@type='password']").send_keys("tester-002")
    driver.find_element(By.XPATH, "//button[contains(@data-test,'login-pwd-next-btn')]").click()

driver.find_element(By.XPATH, "//section[@data-tip='tip-contacts']").click()

driver.find_element(By.XPATH, "//section[@class='navbarMenu navbarMenu_active']").click()
driver.find_element(By.XPATH, "//span[text()='蔡志峰']").click()
driver.find_element(By.XPATH, "//input[@class='larkc-usercard__footer__input larkc-usercard__footer__message-input']")\
                    .send_keys("hello word")
ActionChains(driver).key_down(Keys.ENTER).perform()



# driver.get("http://baidu.com")
# driver.find_element(By.ID, 'kw').send_keys("Python")
# driver.find_element(By.ID, 'su').click()

# 调用 webclient 方法
# WebClient.webclient()
