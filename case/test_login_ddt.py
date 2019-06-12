import os
import unittest
from selenium_html_report.pages.login_page import LoginPage,login_url
from selenium import webdriver
import ddt

"""
用例：
1.输入用户名admin,,密码hyl@qq.com,点击登陆
2.输入用户名admin,点击登录
3.输入密码hyl@qq.com，点击登陆
4.直接点击登陆
5.输入用户名admin,,密码hyl@qq.com,勾选保持登录，点击登陆
6.点击忘记密码
"""
testdates = [
    {"user": "admin", "pwd": "hyl@qq.com", "expect": "admin"},
    {"user": "admin", "pwd": "", "expect": "False"},
    {"user": "", "pwd": "hyl@qq.com", "expect": "False"}
]

@ddt.ddt
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

    def login_test(self, username, pwd, expect):
        self.login_pg.input_username(username)
        self.login_pg.input_pwd(pwd)
        self.login_pg.click_submit()
        result = self.login_pg.get_login_name()
        print("测试结果为：", result)
        self.assertTrue(result == expect)

    #通过读取excel文本，得到testdata
    # project_curpath = os.path.dirname(os.path.realpath(__file__))
    # filepath = os.path.join(project_curpath, "common", "testdata.xlsx")
    # print(filepath)
    # testdata = ExcelUtil(filepath)
    # print(testdata.dict_data())

    ##filepath = r"D:\PycharmProjects\WebDriver\selenium_html_report\common\testdata.xlsx"

    # @ddt.data(*testdates)
    def test01(self):
        """输入用户名admin,,密码hyl@qq.com,点击登陆"""
        print("----------开始测试----------")
        data1 = testdates[0]
        print("测试数据：%s"% data1)
        self.login_test(data1["user"], data1["pwd"], data1["expect"])
        print("-----------pass!!!----------")

    def test02(self):
        """输入用户名admin,点击登录"""
        print("----------开始测试----------")
        data1 = testdates[1]
        print("测试数据：%s" % data1)
        self.login_test(data1["user"], data1["pwd"], data1["expect"])

    def test03(self):
        """输入密码hyl@qq.com，点击登陆"""
        print("----------开始测试----------")
        data1 = testdates[2]
        print("测试数据：%s" % data1)
        self.login_test(data1["user"], data1["pwd"], data1["expect"])

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()