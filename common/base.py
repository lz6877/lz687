

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Base():

    def __init__(self,driver:webdriver.Firefox):
        self.driver = driver
        self.driver.get("http://127.0.0.1:81/zentao/user-login.html")
        self.timeout = 10
        self.t = 1


    def findElement(self,locator):
        if not isinstance(locator, tuple):
            print("locator参数类型错误，必须传元祖类型：loc=('id','value1')")
        else:
            print("正在定位元素信息：定位方式->%s"%(locator[0],locator[1]))
            elel = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_element(*locator))
            return elel

    def findElement2(self,locator):
        elel = WebDriverWait(self.driver,self.timeout,self.t).until(EC.presence_of_element_located(locator))
        return elel

    def sendkeys(self, locator, text):
        elel = self.findElement(locator)
        elel.send_keys(text)

    def click(self,locator):
        elel = self.findElement(locator)
        elel.click()

    def is_Selected(self, locator):
        ele = self.findElement(locator)
        r = ele.is_selected()
        return r

    def isElementExist(self,locator):
        try:
            self.findElement(self,locator)
            return True
        except:
            return False

    """或者通过获取list,判断是否定位到元素"""
    def isElementExist2(self,locator):
        elel = self.findElement(locator)
        n = len(elel)
        if n==1:
            return True
        elif n == 0:
            return False
        else :
            print("定位到的元素有%s个",n)

    """返回boolean值"""
    def is_title(self,locator):
        title = WebDriverWait(self.driver,self.timeout,self.t).until(EC.title_is(locator))
        return title

    def is_title_contains(self,locator):
        title_contains = WebDriverWait(self.driver,self.timeout,self.t).until(EC.title_contains(locator))
        return title_contains

    def is_text_element(self, locator):
        is_text = WebDriverWait(self.driver,self.timeout,self.t).until(EC.text_to_be_present_in_element(locator))
        return is_text

    def is_text_in_element(self, locator, _text):
        try:
            is_text_in = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element(locator, _text))
            return is_text_in
        except:
            return False

    def is_value_in_element(self,locator, value):
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element_value(locator, value))
            return result
        except:
            return False

    #判断是否有alert:
    def is_alert_present(self):
        try:
            is_alert = WebDriverWait(self.driver, self.timeout, self.t).until(EC.alert_is_present())
            return is_alert
        except:
            return False

    #获取文本
    def get_text(self, locator):
        try:
            t = self.findElement(locator).text
            return t
        except:
            print("获取文本失败，返回...")
            return ""

    def js_focus_element(self,locator):
        """"聚焦元素"""
        target = self.findElement(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    def ja_scroll_top(self):
        """滚动到顶部"""
        js = "window.scrollTo(0, 0)"
        self.driver.execute_script(js)

    def js_scroll_end(self):
        """滚动到底部"""
        js = "window.scrollTo(0, document.body.scrollHeight)"
        self.driver.execute_script(js)

    def select_by_index(self, locator, index=0):
        """通过索引，index是索引第几个，从0开始，默认选第一个"""
        element = self.findElement(locator)
        Select(element).select_by_index(index)

    def select_by_value(self, locator,value):
        """通过value属性定位"""
        element = self.findElement(locator)
        Select(element).select_by_value(value)

    def select_by_text(self,locator,text):
        """通过text属性定位"""
        element = self.findElement(locator)
        Select(element).select_by_visible_text(text)


if  __name__ == "__main__":
    driver =webdriver.Firefox()
    zentao = Base(driver)

    locl1 = (By.ID, "account")
    locl2 = (By.NAME, "password")
    locl3 = (By.ID, "submit")

    zentao.sendkeys(locl1)
    zentao.sendkeys(locl2)
    zentao.click()
    zentao.findElement(driver)



