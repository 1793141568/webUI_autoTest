from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
import time


class HomePage(BasePage):
    home_page_username_search_loc=(By.NAME,"username")
    home_page_password_search_loc = (By.CSS_SELECTOR,".pns tr:nth-child(2) td:nth-child(2) input")
    home_page_denglu_search_loc = (By.CSS_SELECTOR, ".pn em")
    home_page_moren_search_loc=(By.CSS_SELECTOR,".bm_c h2 a")
    home_page_subject_search_loc=(By.CSS_SELECTOR,".pbt input")
    home_page_message_search_loc=(By.CSS_SELECTOR,".tedt .area .pt")
    home_page_fabiao_search_loc=(By.CSS_SELECTOR,".ptm strong")
    home_page_huifu_message_search_loc=(By.CSS_SELECTOR,".tedt .pt")
    home_page_huifu_search_loc=(By.CSS_SELECTOR,".ptm .pn strong")



    def denglu(self,user,pwd):
        self.sendkeys(user, *self.home_page_username_search_loc)
        self.sendkeys(pwd, *self.home_page_password_search_loc)
        # self.driver.switch_to.window(self.driver.current_window_handle)
        self.click(*self.home_page_denglu_search_loc)
        time.sleep(3)

        self.click(*self.home_page_moren_search_loc)
    def fatie(self,subject,message,huifu_message):
        self.sendkeys(subject,*self.home_page_subject_search_loc)
        self.sendkeys(message,*self.home_page_message_search_loc)
        self.click(*self.home_page_fabiao_search_loc)
        self.sendkeys(huifu_message,*self.home_page_huifu_message_search_loc)
        self.click(*self.home_page_huifu_search_loc)


