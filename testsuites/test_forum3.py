from testsuites.base_testcase import BaseTestCase
from pageobjects.base import BasePage
from pageobjects.forum3_homepage import HomePage
from  ddt import ddt,data,unpack
import unittest
import time

@ddt
class Forum3(BaseTestCase):

    @data(["haotest"])
    @unpack
    def test_forum3(self,expect_value):
        self.assertEqual(self.driver.title, "论坛 - Powered by Discuz!")
        basepage=BasePage(self.driver)
        # basepage.open_url("http://127.0.0.1/forum.php")
        home_page = HomePage(self.driver)
        home_page.search3("1793141568","zrt++19980928","haotest")
        self.assertEqual(self.driver.title,"搜索 - Discuz! Board - Powered by Discuz!")
        home_page.haotest_tie()
        result=home_page.yanzheng()
        self.assertEqual(result, expect_value, msg=result)

        # basepage.get_windows_img()

