from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
import time

class HomePage(BasePage):
    home_page_username_search_loc=(By.NAME,"username")
    home_page_password_search_loc = (By.CSS_SELECTOR,".pns tr:nth-child(2) td:nth-child(2) input")
    home_page_denglu_search_loc = (By.CSS_SELECTOR, ".pn em")
    home_page_moren_search_loc = (By.CSS_SELECTOR, ".bm_c h2 a")
    home_page_fatie_search_loc=(By.CSS_SELECTOR,"#newspecial img")
    home_page_toupiao_search_loc=(By.LINK_TEXT,"发起投票")
    home_page_subject_search_loc=(By.CSS_SELECTOR,"div.z span input.px")
    home_page_biaoti1_search_loc=(By.CSS_SELECTOR,".mbm p:first-of-type input")
    home_page_biaoti2_search_loc=(By.CSS_SELECTOR,".mbm p:nth-child(2) input")
    home_page_biaoti3_search_loc=(By.CSS_SELECTOR,".mbm p:nth-child(3) input")
    home_page_postsubmit_search_loc=(By.CSS_SELECTOR,".mtm button#postsubmit span")
    home_page_input_option1_search_loc=(By.CSS_SELECTOR,"tbody  input#option_1")
    home_page_submit_search_loc=(By.CSS_SELECTOR,"button.pn span")
    home_page_xuanxiang1_search_loc=(By.CSS_SELECTOR,"div.pcht tbody tr:first-of-type  label")
    home_page_bili1_search_loc=(By.CSS_SELECTOR,"div.pcht table tr:nth-child(2) td:nth-child(2)")
    home_page_xuanxiang2_search_loc=(By.CSS_SELECTOR,"div.pcht tbody tr:nth-child(3)  label")
    home_page_bili2_search_loc = (By.CSS_SELECTOR, "div.pcht table tr:nth-child(4) td:nth-child(2)")
    home_page_xuanxiang3_search_loc = (By.CSS_SELECTOR, "div.pcht tbody tr:nth-child(5)  label")
    home_page_bili3_search_loc = (By.CSS_SELECTOR, "div.pcht table tr:nth-child(6) td:nth-child(2)")
    home_page_zhuti_search_loc=(By.CSS_SELECTOR,"h1.ts span")




    def search4(self,user,pwd,subject,biaoti1,biaoti2,biaoti3):
        #用户登录
        self.sendkeys(user, *self.home_page_username_search_loc)
        self.sendkeys(pwd, *self.home_page_password_search_loc)
        self.click(*self.home_page_denglu_search_loc)
        time.sleep(2)
        self.click(*self.home_page_moren_search_loc)  #点击默认板块
        time.sleep(2)
        self.xuanting(*self.home_page_fatie_search_loc)    #鼠标发帖处悬停
        self.click(*self.home_page_toupiao_search_loc)     #点击发起投票链接
        time.sleep(3)
        self.sendkeys(subject,*self.home_page_subject_search_loc)   #输入帖子标题
        self.sendkeys(biaoti1,*self.home_page_biaoti1_search_loc)
        self.sendkeys(biaoti2, *self.home_page_biaoti2_search_loc)     #输入投票选项
        self.sendkeys(biaoti3, *self.home_page_biaoti3_search_loc)

        self.click(*self.home_page_postsubmit_search_loc)   #点击发起投票按钮
        time.sleep(3)
        self.click(*self.home_page_input_option1_search_loc)
        self.click(*self.home_page_submit_search_loc)       #点击投票
        time.sleep(2)
        print(self.text(*self.home_page_xuanxiang1_search_loc), self.text(*self.home_page_bili1_search_loc))
        print(self.text(*self.home_page_xuanxiang2_search_loc), self.text(*self.home_page_bili2_search_loc))
        print(self.text(*self.home_page_xuanxiang3_search_loc), self.text(*self.home_page_bili3_search_loc))
        print(self.text(*self.home_page_zhuti_search_loc))     #取出投票各个选项的名称和投票比例以及主题名称


        time.sleep(2)

















