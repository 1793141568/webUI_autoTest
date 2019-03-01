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
        basepage=BasePage(self.driver)
        # basepage.open_url("http://127.0.0.1/forum.php")
        home_page = HomePage(self.driver)
        home_page.search3("1793141568","zrt++19980928","haotest")
        result=home_page.yanzheng()
        self.assertEqual(result, expect_value, msg=result)

        # basepage.get_windows_img()

