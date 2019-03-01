from testsuites.base_testcase import BaseTestCase
from pageobjects.base import BasePage
from pageobjects.forum2_homepage import HomePage
import unittest
import time


class Forum2(BaseTestCase):

    def test_forum2(self):
        basepage=BasePage(self.driver)
        # basepage.open_url("http://127.0.0.1/forum.php")
        home_page = HomePage(self.driver)
        home_page.admin_search2("admin","123456","123456","喜刷刷")
        home_page.user_search2("1793141568","zrt++19980928","用户贴","老魔王闲来无事来发帖，进来的都是精英","沙发糖果都是俺的")
        # basepage.get_windows_img()

