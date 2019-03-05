from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import unittest
from ddt import ddt,data,unpack
from framework.util import Util
import time
import os

testdata = Util.read_excel(os.path.dirname(os.path.realpath(__file__))+"\../framework\data.xlsx")
@ddt
class Search_by_ddt(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('../tools/chromedriver.exe')
        self.driver.maximize_window()
        self.driver.get("https://www.baidu.com")
        self.driver.implicitly_wait(5)
        # print("开始测试")
    @data(*testdata)
    def test_search_by_ddt(self,data):
        search_string=data['姓名']
        print("搜索内容：%s"%search_string)
        search_input=self.driver.find_element_by_id("kw")

        search_input.send_keys(search_string+Keys.ENTER)
        time.sleep(5)
        search_input.submit()
    def tearDown(self):
        self.driver.quit()
        # pass

if __name__=="__main__":
    unittest.main()