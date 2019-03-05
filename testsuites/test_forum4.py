from testsuites.base_testcase import BaseTestCase
from pageobjects.base import BasePage
from pageobjects.forum4_homepage import HomePage
import unittest
import time



class Forum4(BaseTestCase):

    def test_forum4(self):
        self.assertEqual(self.driver.title, "论坛 - Powered by Discuz!")
        basepage=BasePage(self.driver)
        # basepage.open_url("http://127.0.0.1/forum.php")
        home_page = HomePage(self.driver)
        home_page.search4("admin","123456",)
        self.assertEqual(self.driver.title,"【新提醒】发表帖子 - 默认版块 - Discuz! Board - Powered by Discuz!")
        home_page.toupiaotie("大家的表情","笑","哭","酷")
        self.assertEqual(self.driver.title,"【新提醒】大家的表情 - 默认版块 - Discuz! Board - Powered by Discuz!")
        home_page.shuchu()

        # basepage.get_windows_img()

