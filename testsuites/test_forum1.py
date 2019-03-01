from testsuites.base_testcase import BaseTestCase
from pageobjects.base import BasePage
from pageobjects.forum1_homepage import HomePage
import unittest
import time


class Forum1(BaseTestCase):

    def test_forum1(self):
        basepage=BasePage(self.driver)
        # basepage.open_url("http://127.0.0.1/forum.php")
        home_page = HomePage(self.driver)
        home_page.search1("admin","123456","第一次发帖","好激动ssssssssssssssssss","你好666啊")
        # basepage.get_windows_img()

