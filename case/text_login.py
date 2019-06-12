import unittest
from selenium_html_report.pages.login_page import LoginPage,login_url
from selenium import webdriver

"""
用例：
1.输入用户名admin,,密码hyl@qq.com,点击登陆
2.输入用户名admin,点击登录
3.输入密码hyl@qq.com，点击登陆
4.直接点击登陆
5.输入用户名admin,,密码hyl@qq.com,勾选保持登录，点击登陆
6.点击忘记密码
"""

class LoginPageTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.login_pg = LoginPage(cls.driver)

    def setUp(self):
        self.driver.get(login_url)
        self.login_pg.is_alert_exist()
        self.driver.delete_all_cookies()
        self.driver.refresh()

    def test01(self):
        """输入用户名admin,,密码hyl@qq.com,点击登陆"""
        self.login_pg.input_username("admin")
        self.login_pg.input_pwd("hyl@qq.com")
        self.login_pg.click_submit()
        result = self.login_pg.get_login_name()
        print("当前用户为：", result)
        self.assertTrue(result == "admin")

    def test02(self):
        """输入用户名admin,点击登录"""
        self.login_pg.input_username("admin")
        self.login_pg.click_submit()
        result = self.login_pg.get_login_name()
        print("当前用户为：", result)
        self.assertTrue(result == "")

    def test03(self):
        """输入密码hyl@qq.com，点击登陆"""
        self.login_pg.input_pwd("hyl@qq.com")
        self.login_pg.click_submit()
        result = self.login_pg.get_login_name()
        print("当前用户为：", result)
        self.assertTrue(result == "")

    def test04(self):
        """直接点击登陆"""
        self.login_pg.click_submit()
        result = self.login_pg.get_login_name()
        print("当前用户为：", result)
        self.assertTrue(result == "")

    def test05(self):
        """输入用户名admin,,密码hyl@qq.com,勾选保持登录，点击登陆"""
        self.login_pg.input_username("admin")
        self.login_pg.input_pwd("hyl@qq.com")
        self.login_pg.click_keep_login()
        self.login_pg.click_submit()
        result = self.login_pg.get_login_name()
        print("当前用户为：", result)
        self.assertTrue(result == "admin")

    def test06(self):
        """直接点击忘记密码"""
        self.login_pg.click_forget()
        result = self.login_pg.is_refresh_exist()
        self.assertTrue(result)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()