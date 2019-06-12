import unittest
import time

from selenium import webdriver
from pages.add_bug_page import ZenTaoBug
from pages.login_page import LoginPage

class Test_Add_Bug(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.zentaobug = ZenTaoBug(cls.driver)
        a = LoginPage(cls.driver)
        a.is_loginfuc()

    def test_add_bug(self):
        timestr = time.strftime("%Y/%m/%D %H:%M:%S")
        title = "测试bug" + timestr
        self.zentaobug.addBug(title)
        result = self.zentaobug.is_add_bug_sucess(title)
        print(result)
        self.assertTrue(result)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()