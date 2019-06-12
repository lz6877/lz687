#coding:utf-8
import unittest
import time
from selenium import webdriver
from case.zentaologin import Base

login_url = "http://127.0.0.1:81/zentao/user-login.html"


class LoginPage(Base):  #继承

    #登录
    locl_user = ("id","account")
    locl_pwd = ("css selector", "[name='password']")
    locl_submit = ("xpath", "//*[@id='submit']")
    locl_keep_login = ("id", "keepLoginon")
    locl_forget = ("link text", "忘记密码")
    locl_get_user = ("xpath", "//*[@id='userNav']/li/a/span[1]")
    locl_forget_pwd_page = ("xpath", "html/body/div[1]/div/div[2]/div[2]/a")


    def input_username(self, _text):
        self.sendkeys(self.locl_user, _text)

    def input_pwd(self, _text):
        self.sendkeys(self.locl_pwd, _text)

    def click_submit(self):
        self.click(self.locl_submit)

    def click_keep_login(self):
        self.click(self.locl_keep_login)

    def click_forget(self):
        self.click(self.locl_forget)

    def is_alert_exist(self):
        """判断alert是否存在"""
        try:
            time.sleep(3)
            alert = self.driver.switch_to.alert()
            text = alert.text
            alert.accept()
            return text
        except:
            return ""

    def get_login_reslut(self,text):
        """判断是否获得登录后的用户名，返回boolean值"""
        result = self.is_text_element(self.locl_get_user, text)
        return result

    def is_loginfuc(self, username="admin", pwd="hyl@qq.com", keep_login=False):
        """登录函数流程"""
        self.driver.get(login_url)
        self.input_username(username)
        self.input_pwd(pwd)
        if keep_login:
            self.click_keep_login()
        self.click_submit()


    def is_refresh_exist(self):
        """忘记密码，刷新页面是否存在"""
        r = self.isElementExist(self.locl_forget_pwd_page)
        return r

    def get_login_name(self):
        """是否能获取到当前账户名，返回字符串结果"""
        try:
            r = self.findElement(self.locl_get_user).text
            return r
        except:
             return "False"


if __name__ == "__main__" :
    driver = webdriver.Firefox()
    driver.get(login_url)
    loginpage = LoginPage(driver)
    loginpage.input_username("admin")
    loginpage.input_pwd("hyl@qq.com")
    loginpage.click_submit()
    time.sleep(5)
    result = loginpage.get_login_name()
    print("当前账户名为：", result)









