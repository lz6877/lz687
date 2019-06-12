#coding:utf-8
import unittest
import time
from selenium import webdriver
from selenium_html_report.case.zentaologin import Base
driver = webdriver.Firefox()


class ZenTaoBug(Base):  #继承

    #登录
    locl1 = ("id","account")
    locl2 = ("css selector", "[name='password']")
    locl3 = ("xpath", "//*[@id='submit']")

    #提bug
    lo_test = ("link text", "测试")
    lo_bug = ("xpath", "//*[@id='subNavbar']/ul/li[1]/a")
    lo_add_bug = ("xpath", "//*[@id='mainMenu']/div[3]/a[3]")
    lo_truck = ("xpath", "//*[@id='openedBuild_chosen']/ul")
    lo_truck_add = ("xpath","//*[@id='openedBuild_chosen']/div/ul/li")
    lo_input_title = ("id","title")
    #需先切换
    lo_input_body = ("class name", "article-content")
    lo_save = ("id", "submit")

    #新增的列
    lo_new = ("xpath", "//*[@id='bugList']/tbody/tr[1]/td[4]/a")

    def login(self,username="admin", password="hyl@qq.com"):
        self.sendkeys(self.locl1, username)
        self.sendkeys(self.locl2, password)
        self.click(self.locl3)

    def addBug(self, title):
        self.click(self.lo_test)
        time.sleep(3)
        self.click(self.lo_bug)
        time.sleep(3)
        self.click(self.lo_add_bug)
        self.click(self.lo_truck)
        self.click(self.lo_truck_add)
        self.sendkeys(self.lo_input_title, title)

        #输入body
        frame = self.findElement(("class name", "ke-edit-iframe"))
        self.driver.switch_to.frame(frame)
        time.sleep(3)

        body = """[测试步骤]xxx
        [结果]xxx
        [期望结果]xxx
        """

        self.sendkeys(self.lo_input_body, body)
        self.driver.switch_to.default_content()
        time.sleep(5)
        self.click(self.lo_save)

    def is_add_bug_sucess(self, _text):
        print(_text)
        return self.is_text_in_element(self.lo_new, _text)

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:81/zentao/user-login.html")
    zentaobug = ZenTaoBug(driver)
    zentaobug.login()
    timestr = time.strftime("%Y/%m/%D %H:%M:%S")
    title = "测试bug" + timestr
    zentaobug.addBug(title)
    result = zentaobug.is_add_bug_sucess(title)
    print(result)






