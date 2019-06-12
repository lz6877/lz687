import time
import unittest
from selenium import webdriver

from selenium_html_report.common.loginfunc import loginFunction

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    # def get_login_name(self):
    #     try:
    #         userName = self.driver.find_element_by_xpath("//*[@id='userNav']/li/a/span[1]").text
    #         print("当前用户名为：", userName)
    #         return userName
    #     except:
    #         return ""

    def is_alert(self):
        """判断是否有弹出框"""
        time.sleep(3)
        try:
            is_alert = self.driver.switch_to.alert()
            t = is_alert.text
            print(t)
            is_alert.accept
            return t
        except:
            return ""

    def test_login01(self):
        loginFunction(self.driver)
        time.sleep(3)
        # userName = self.driver.find_element_by_xpath("//*[@id='userNav']/li/a/span[1]").text
        # print("当前用户名为：", userName)

    def tearDown(self):
        self.is_alert()
        self.driver.quit()
        #self.driver.delete_all_cookies()

if __name__ == "__main__":
    unittest.main()