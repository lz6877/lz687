# coding:utf-8
import time
import unittest
from selenium import webdriver


class Logintest(unittest.TestCase):

    # 打开浏览器：
    def setUp(self):
        self.driver = webdriver.Firefox()
        url = "http://127.0.0.1:81/zentao/user-login.html"
        self.driver.get(url)

    def get_login_userName(self):
        try:
            t = self.driver.find_element_by_xpath("//*[@id='userNav']/li/a/span[1]").text
            print(t)
            return t
        except:
            return ""

    def is_alert_exist(self):
        """判断alert是否存在"""
        try:
            time.sleep(3)
            alert = self.driver.switch_to.alert
            text = alert.text
            alert.accept()
            return text
        except:
            return ""

    def test_1(self):
        time.sleep(3)

        self.driver.find_element_by_id("account").send_keys("admin")
        self.driver.find_element_by_name("password").send_keys("hyl@qq.com")
        time.sleep(2)
        self.driver.find_element_by_id("submit").click()
        time.sleep(3)
        t = self.get_login_userName()
        print("获取登录后的用户名：", t)
        self.assertTrue(t == "admin")

    def test_2(self):
        time.sleep(3)

        self.driver.find_element_by_id("account").send_keys("admin1")
        self.driver.find_element_by_name("password").send_keys("hyl@qq.com1")
        time.sleep(2)
        self.driver.find_element_by_id("submit").click()
        t = self.get_login_userName()
        print("获取失败的用户名：", t)
        self.assertTrue(1 == 2)

    def tearDown(self):
        self.is_alert_exist()
        self.driver.quit()
        #self.driver.delete_all_cookies()  # 清除所有cookies，退出操作

if __name__=="__main__":
    unittest.main()