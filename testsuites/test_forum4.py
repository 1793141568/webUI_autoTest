from testsuites.base_testcase import BaseTestCase
from pageobjects.base import BasePage
from pageobjects.forum4_homepage import HomePage
import unittest
import time



class Forum4(BaseTestCase):

    def test_forum4(self):
        basepage=BasePage(self.driver)
        # basepage.open_url("http://127.0.0.1/forum.php")
        home_page = HomePage(self.driver)
        home_page.search4("admin","123456","大家的表情","笑","哭","酷")
        # basepage.get_windows_img()

