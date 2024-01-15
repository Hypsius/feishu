import yaml
from appium.webdriver import webdriver
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium import webdriver


# 需要用户登录过账号后进行自动化
class AndroidClient(object):
    driver: webdriver

    @classmethod
    # yaml数据驱动初始类
    def initDriver(cls, key) -> webdriver:
        # 最新版YAML需要指定Loader解析器：SafeLoader、FullLoader
        driver_data = yaml.load(open('../data/driver.yaml'), Loader=yaml.FullLoader)
        platform = str(driver_data['platform'])
        cls.platform = platform
        caps = driver_data[key]['caps'][platform]
        server = driver_data[key]['server']
        implicitly_wait = driver_data[key]['implicitly_wait']
        options = UiAutomator2Options().load_capabilities(caps)
        cls.driver = webdriver.Remote(server, options=options)
        cls.driver.implicitly_wait(implicitly_wait)
        return cls.driver

    @classmethod
    def restart_app(cls) -> webdriver:
        # caps = {}
        # caps['platformName'] = 'Android'
        # caps['deviceName'] = 'huawei'
        # caps['appPackage'] = 'com.ss.android.lark'
        # caps['appActivity'] = '.main.app.MainActivity'
        # caps['automationName'] = 'UiAutomator2'
        # caps['platformVersion'] = '12'
        # #为了更快的启动，保留之前的数据，从而可以保存上一个case执行后的状态
        # caps['noReset'] = 'true'
        # caps['uuid'] = '127.0.0.1:7555'
        #
        # options = UiAutomator2Options().load_capabilities(caps)
        # cls.driver = webdriver.Remote('http://localhost:4723', options=options)
        return cls.initDriver('restart_app')

    @classmethod
    # 进行第一次启动
    def install_app(cls) -> webdriver:
        caps = {}
        caps['platformName'] = 'Android'
        caps['deviceName'] = 'huawei'
        caps['appPackage'] = 'com.ss.android.lark'
        caps['appActivity'] = '.main.app.MainActivity'
        caps['automationName'] = 'UiAutomator2'
        caps['platformVersion'] = '12'
        #解决第一次启动的授权问题
        caps["autoGrantPermissions"] = "true"
        caps['noReset'] = 'true'
        caps['uuid'] = '127.0.0.1:7555'

        options = UiAutomator2Options().load_capabilities(caps)
        cls.driver = webdriver.Remote('http://localhost:4723', options=options)
        # return cls.initDriver('install_app')


AndroidClient.install_app()
# AndroidClient.restart_app()


class WebClient(object):
    driver: webdriver

    @classmethod
    def initDriver(cls, key) -> webdriver:
        # 最新版YAML需要指定Loader解析器：SafeLoader、FullLoader
        driver_data = yaml.load(open('../data/WebDriver.yaml'), Loader=yaml.FullLoader)
        options = webdriver.ChromeOptions()
        if key == 'restart_app':
            file = driver_data[key]['local file']
            options.add_argument(file)  # 使用已经登录过的chrome浏览器实例，实现cookie免登录
        options.add_experimental_option("detach", True)     # 执行完实例后不自动关闭浏览器，需要关闭可使用close函数
        cls.driver = webdriver.Chrome(options=options)
        server = driver_data[key]['server']
        cls.driver.get(server)
        implicitly_wait = driver_data[key]['implicitly_wait']
        cls.driver.implicitly_wait(implicitly_wait)
        return cls.driver

    @classmethod
    def restart_app(cls) -> webdriver:
        return cls.initDriver('restart_app')

    @classmethod
    def install_app(cls) -> webdriver:
        return cls.initDriver('install_app')


# WebClient().install_app()
# WebClient().restart_app()

