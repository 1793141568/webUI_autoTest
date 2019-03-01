import os.path
from configparser import ConfigParser
from selenium import webdriver
from framework.logger import Logger

logger=Logger(logger="BrowserEngine").getlog()

class BrowserEngine(object):
    # 相对路径获取方法
    dir = os.path.dirname(os.path.abspath("."))
    chrome_driver_path = dir + "/tools/chromedriver.exe"
    ie_driver_path = dir + "/tools/IEDdriverServer.exe"
    firefox_driver_path = dir + "/tools/geckodriver.exe"

    # 从config.ini文件读取浏览器类型，返回驱动程序
    def open_browser(self):
        config = ConfigParser()
        file_path = os.path.dirname(os.path.abspath(".")) + "/config/config.ini"
        config.read(file_path)

        browser = config.get("browserType", "browserName")
        logger.info("你选择了%s浏览器" % browser)  # you had selectt %s browser
        url = config.get("testServer", "URL")
        logger.info("测试URL是:%s" % url)  # the test server url is

        if browser == "Firefox":
            driver = webdriver.Firefox(self.firefox_driver_path)  # 启动Firefox
            logger.info("启动火狐浏览器")
        elif browser == "Chrome":
            driver = webdriver.Chrome(self.chrome_driver_path)
            logger.info("启动谷歌浏览器")
        elif browser == "IE":
            driver = webdriver.Ie(self.ie_driver_path)
            logger.info("启动IE浏览器")

        driver.get(url)
        logger.info("打开：%s" % url)
        driver.maximize_window()
        logger.info("窗口最大化")
        driver.implicitly_wait(10)
        logger.info("等待10秒")
        return driver

    def quit_browser(self):
        self.driver.quit()
        logger.info("关闭浏览器")

