import yaml
from appium.webdriver import webdriver
from appium import webdriver
from appium.options.android import UiAutomator2Options


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
        # caps = {}
        # caps['platformName'] = 'Android'
        # caps['deviceName'] = 'huawei'
        # caps['appPackage'] = 'com.ss.android.lark'
        # caps['appActivity'] = '.main.app.MainActivity'
        # caps['automationName'] = 'UiAutomator2'
        # caps['platformVersion'] = '12'
        # #解决第一次启动的授权问题
        # caps["autoGrantPermissions"] = "true"
        # caps['noReset'] = 'true'
        # caps['uuid'] = '127.0.0.1:7555'
        #
        # options = UiAutomator2Options().load_capabilities(caps)
        # cls.driver = webdriver.Remote('http://localhost:4723', options=options)
        return cls.initDriver('install_app')


# AndroidClient.install_app()
# AndroidClient.restart_app()


