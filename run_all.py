# import unittest
# from lz687_auto.common import HTMLTestRunner_cn
#
# #用例路径
# casePath = "D:\Program Files\Github\lz687_auto\case"
# rule = "test*.py"
# discover = unittest.defaultTestLoader.discover(start_dir=casePath, pattern=rule)
# print(discover)
#
# reportPath = r"D:\PycharmProjects\WebDriver\selenium_html_report\report"+"report.html"
#
# fp = open(reportPath, "wb")
# runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp, title="禅道登录功能的测试", description="禅道测试登录功能测试")
#
# runner.run(discover)
#
# fp.close()


import unittest

import sys
import os
current_path = os.path.dirname(os.path.abspath(__file__))  #获取当前run_all.py的绝对路径
sys.path.append("D:\Program Files\Github\lz687_auto")
print(sys.path)
from lz687_auto.common import HTMLTestRunner_cn


#用例路径
casePath = "D:\PycharmProjects\WebDriver\selenium_html_report\case"
rule = "test01.py"
discover = unittest.defaultTestLoader.discover(start_dir=casePath, pattern=rule)

reportPath = r"D:\PycharmProjects\WebDriver\selenium_html_report\report"+"report1.html"

fp = open(reportPath, "wb")

runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp, title="", description="")

runner.run(discover)

