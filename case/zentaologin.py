

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Base():

    def __init__(self,driver:webdriver.Firefox):
        self.driver = driver
        self.driver.get("http://127.0.0.1:81/zentao/user-login.html")
        self.timeout = 10
        self.t = 1


    def findElement(self,locator):
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



