from selenium import webdriver
from framework.browser_engine import BrowserEngine
import unittest

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        browserengine = BrowserEngine()
        self.driver = browserengine.open_browser()
        # self.driver = webdriver.Chrome('../tools/chromedriver.exe')
        # self.driver.maximize_window()
        # self.driver.implicitly_wait(5)
    def tearDown(self):
        self.driver.quit()