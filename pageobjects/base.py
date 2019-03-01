from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from framework.logger import Logger
from  selenium.webdriver.common.action_chains import ActionChains
import time
import os
from selenium import webdriver
logger=Logger(logger="BasePage").getlog()
class BasePage(object):
    def __init__(self,driver):
        self.driver=driver
    #浏览器后退按钮
    def back(self):
        self.driver.back()
    #浏览器前进按钮
    def forward(self):
        self.driver.forward()
    def open_url(self,url):
        self.driver.get(url)
    def quit_browser(self):
        self.driver.quit()
    def cloce(self):
        try:
            self.driver.close()
            logger.info("关闭页面")
        except Exception as e:
            self.get_windows_img()
            logger.error("关闭页面异常 %s"% e)
    def find_element(self, *loc):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
            logger.info("找到页面元素—%s",loc)
        except:
            logger.error("%s页面中没有找到%s元素"%(self,loc))
    def sendkeys(self,text,*loc):
        el=self.find_element(*loc)
        # el.clear()
        try:
            el.send_keys(text)
            logger.info("输入内容：%s成功"%text)
        except Exception as e:
             logger.error("输入异常--%s"%e)
             self.get_windows_img()
    def clear(self,*loc):
        el=self.find_element(*loc)
        try:
            el.clear()
            logger.info("清除成功")
        except Exception as e:
            logger.error("清除异常--%s"%e)
            self.get_windows_img()
    def click(self,*loc):
        el = self.find_element(*loc)
        try:
            el.click()
            logger.info("点击成功")
        except Exception as e:
            logger.error("点击异常--%s" % e)

    def get_windows_img(self):
        file_path = os.path.dirname(os.path.abspath(".")) + '/screenshorts/'
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("get_windows_img")
        except:
            self.get_windows_img()
            logger.error("not get_windows_img")
    def xuanting(self,*loc):
        el = self.find_element(*loc)
        try:
            ActionChains(self.driver).move_to_element(el).perform()
            logger.info("悬停成功")
        except Exception as e:
            logger.error("悬停异常--%s" % e)
    def jinru_iframe(self,loc):     #切换到iframe
        self.driver.switch_to.frame(loc)
    def tuichu_iframe(self):
        self.driver.switch_to.default_content()
    def text(self,*loc):
        el = self.find_element(*loc)
        try:
            return el.text
            logger.info("输出文本成功")
        except Exception as e:
            logger.error("输出文本异常--%s" % e)
    def quit(self):
        try:
            self.driver.quit()
            logger.info("关闭浏览器")
        except Exception as e:
            logger.error("关闭浏览器异常 %s"% e)