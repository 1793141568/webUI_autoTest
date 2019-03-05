from testsuites.base_testcase import BaseTestCase
from pageobjects.base import BasePage
from pageobjects.forum2_homepage import HomePage
import unittest
import time


class Forum2(BaseTestCase):

    def test_forum2(self):
        self.assertEqual(self.driver.title, "论坛 - Powered by Discuz!")
        basepage=BasePage(self.driver)
        # basepage.open_url("http://127.0.0.1/forum.php")
        home_page = HomePage(self.driver)
        home_page.admin_denglu("admin","123456")
        self.assertEqual(self.driver.title, "【新提醒】默认版块 - Discuz! Board - Powered by Discuz!")
        home_page.admin_shanchu("123456")
        self.assertEqual(self.driver.title,"Discuz! Board 管理中心 - 论坛 - 版块管理")
        home_page.admin_xinbankuai("喜刷刷")
        home_page.user_denglu("1793141568","zrt++19980928")
        self.assertEqual(self.driver.title,"喜刷刷 - Discuz! Board - Powered by Discuz!")
        home_page.user_fabiao("用户贴","老魔王闲来无事来发帖，进来的都是精英")
        self.assertEqual(self.driver.title,"用户贴 - 喜刷刷 - Discuz! Board - Powered by Discuz!")
        home_page.user_huifu("沙发糖果都是俺的")
        # basepage.get_windows_img()

