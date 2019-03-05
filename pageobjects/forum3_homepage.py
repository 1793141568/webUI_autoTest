from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
import time

class HomePage(BasePage):
    home_page_username_search_loc=(By.NAME,"username")
    home_page_password_search_loc = (By.CSS_SELECTOR,".pns tr:nth-child(2) td:nth-child(2) input")
    home_page_denglu_search_loc = (By.CSS_SELECTOR, ".pn em")
    home_page_srchtxt__search_loc=(By.CSS_SELECTOR,"td.scbar_txt_td input")
    home_page_searchsubmint_search_loc=(By.CSS_SELECTOR,".scbar_btn_td button")
    home_page_haoster_search_loc=(By.CSS_SELECTOR,".xs3 font")
    home_page_biaoti_search_loc=(By.CSS_SELECTOR,".ts span")




    def search3(self,user,pwd,srchtxt):
        #用户登录
        self.sendkeys(user, *self.home_page_username_search_loc)
        self.sendkeys(pwd, *self.home_page_password_search_loc)
        self.click(*self.home_page_denglu_search_loc)
        time.sleep(2)
        #用户搜索
        self.sendkeys(srchtxt,*self.home_page_srchtxt__search_loc)
        self.click(*self.home_page_searchsubmint_search_loc)
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[1])
    def haotest_tie(self):
        #进入haoster帖子
        self.click(*self.home_page_haoster_search_loc)
        self.driver.switch_to.window(self.driver.window_handles[2])
        time.sleep(4)
    def yanzheng(self):
        a=self.driver.find_element_by_css_selector(".ts span")
        return a.text






