import yaml
from selenium import webdriver


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