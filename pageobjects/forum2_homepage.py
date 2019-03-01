from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
import time

class HomePage(BasePage):
    #管理员
    home_page_username_search_loc=(By.NAME,"username")
    home_page_password_search_loc = (By.CSS_SELECTOR,".pns tr:nth-child(2) td:nth-child(2) input")
    home_page_denglu_search_loc = (By.CSS_SELECTOR, ".pn em")
    home_page_moren_search_loc=(By.CSS_SELECTOR,".bm_c h2 a")
    home_page_input_search_loc=(By.CSS_SELECTOR,"table#threadlisttableid tbody:nth-child(2) input")
    home_page_delete_search_loc=(By.LINK_TEXT,"删除")
    home_page_OK_search_loc = (By.CSS_SELECTOR, ".pnc span")
    home_page_guanli_search_loc=(By.LINK_TEXT,"管理中心")
    home_page_admin_password_search_loc=(By.NAME,"admin_password")
    home_page_tijiao_search_loc=(By.NAME,"submit")
    home_page_forum_search_loc=(By.CSS_SELECTOR,".nav ul li:nth-child(7) a")
    home_page_add_search_loc=(By.LINK_TEXT,"添加新版块")
    home_page_mingcheng_search_loc=(By.CSS_SELECTOR,"body form table tbody:nth-last-child(2) tr:nth-last-child(2) .board input")
    home_page_admin_tijiao_search_loc=(By.CSS_SELECTOR,"div.fixsel input")
    home_page_admin_tuichu_search_loc=(By.LINK_TEXT,"退出")
    #用户
    home_page_shouye_search_loc=(By.CSS_SELECTOR,"div#wp div.z a.nvhm")
    home_page_xinbankuai_search_loc=(By.CSS_SELECTOR,"tbody tr.fl_row:nth-last-child(2) h2 a")
    home_page_subject_search_loc = (By.CSS_SELECTOR, ".pbt input")
    home_page_message_search_loc = (By.CSS_SELECTOR, ".tedt .area .pt")
    home_page_fabiao_search_loc = (By.CSS_SELECTOR, ".ptm strong")
    home_page_huifu_message_search_loc = (By.CSS_SELECTOR, ".tedt .pt")
    home_page_huifu_search_loc = (By.CSS_SELECTOR, ".ptm .pn strong")
    home_page_tuichu_search_loc=(By.LINK_TEXT,"退出")



    def admin_search2(self,user,pwd,admin_password,mingcheng):
        #管理员登录
        self.sendkeys(user, *self.home_page_username_search_loc)
        self.sendkeys(pwd, *self.home_page_password_search_loc)
        self.click(*self.home_page_denglu_search_loc)
        time.sleep(3)
        self.click(*self.home_page_moren_search_loc)
        time.sleep(2)


        #删帖
        self.click(*self.home_page_input_search_loc)
        time.sleep(2)
        self.click(*self.home_page_delete_search_loc)
        time.sleep(2)
        self.click(*self.home_page_OK_search_loc)
        time.sleep(1)

        #进入管理中心
        self.click(*self.home_page_guanli_search_loc)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.sendkeys(admin_password,*self.home_page_admin_password_search_loc)
        self.click(*self.home_page_tijiao_search_loc)
        self.click(*self.home_page_forum_search_loc)
        self.driver.switch_to.frame(0)
        time.sleep(2)

        #添加新版块
        self.click(*self.home_page_add_search_loc)
        time.sleep(2)
        self.clear(*self.home_page_mingcheng_search_loc)
        self.sendkeys(mingcheng,*self.home_page_mingcheng_search_loc)
        self.click(*self.home_page_admin_tijiao_search_loc)
        time.sleep(5)
        self.cloce()
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.click(*self.home_page_admin_tuichu_search_loc)
        time.sleep(5)
    def user_search2(self,user1,pwd1,subject,message,huifu_message):
        # 用户登录
        self.sendkeys(user1, *self.home_page_username_search_loc)
        self.sendkeys(pwd1, *self.home_page_password_search_loc)
        self.click(*self.home_page_denglu_search_loc)
        time.sleep(3)
        #进入首页
        self.click(*self.home_page_shouye_search_loc)
        #进入新版块 发表帖子  回复帖子
        self.click(*self.home_page_xinbankuai_search_loc)
        self.sendkeys(subject, *self.home_page_subject_search_loc)
        self.sendkeys(message, *self.home_page_message_search_loc)
        self.click(*self.home_page_fabiao_search_loc)
        self.sendkeys(huifu_message, *self.home_page_huifu_message_search_loc)
        time.sleep(20)
        self.click(*self.home_page_huifu_search_loc)
        self.click(*self.home_page_tuichu_search_loc)


