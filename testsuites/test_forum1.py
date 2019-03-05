from testsuites.base_testcase import BaseTestCase
from pageobjects.base import BasePage
from pageobjects.forum1_homepage import HomePage
import unittest
import time


class Forum1(BaseTestCase):

    def test_forum1(self):
        self.assertEqual(self.driver.title, "论坛 - Powered by Discuz!")
        basepage=BasePage(self.driver)
        # basepage.open_url("http://127.0.0.1/forum.php")
        home_page = HomePage(self.driver)
        home_page.denglu("admin","123456")
        self.assertEqual(self.driver.title,"默认版块 - Discuz! Board - Powered by Discuz!")
        home_page.fatie("第一次发帖","好激动ssssssssssssssssss","你好666啊")
        # basepage.get_windows_img()

