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
import time
import sys
import os
import smtplib
from common import HTMLTestRunner_cn
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
#from tomorrow import threading
"""若报告出现乱码，可加上以下两行代码："""
# reload(sys)
# sys.setdefaultencoding("utf-8")

#优化版执行所有用例并发送报告，分四步骤
#第一步加载用例
#第二步执行用例
#第三步获取最新测试报告
#第四步发送邮箱

#当前脚本所在文件真实路径
current_path = os.path.dirname(os.path.abspath(__file__))  #获取当前run_all.py的绝对路径
print(current_path)
#rule = "test_login_ddt.py"

def add_case(caseName="case", rule="test_login_ddt.py"):
    """第一步加载所有的测试用例"""
    case_path = os.path.join(current_path, caseName)
    '''如果不存在case文件夹，则新建一个'''
    if not os.path.exists(case_path):
        os.mkdir(case_path)
    """定义discover方法的参数"""
    discover = unittest.defaultTestLoader.discover(start_dir=case_path, pattern=rule, top_level_dir=None)
    return discover

def run_case(all_case, reportName="report"):
    """第二步，执行所有的用例，并把结果写入HTML测试报告中"""
    now_time = time.strftime("%Y/%m%D %H:%M:%S")
    reportPath = os.path.join(current_path, reportName)  #用例文件夹路径
    if not os.path.exists(reportPath):
        os.mkdir(reportPath)
    reportPath = os.path.join(reportPath, "result.html")
    fp = open(reportPath, "wb")
    runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp, verbosity=2, title="zen tao 功能测试", description="")
    runner.run(all_case)      #调用all_case
    fp.close()

def get_report_file(reportPath):
    """获取最新的测试报告"""
    lists = os.listdir(reportPath)
    lists.sort(key=lambda fn:os.path.getmtime(os.path.join(reportPath,fn)))
    print(u"最新测试生成的报告："+ lists[-1])
    #找到最新生成的报告文件
    report_file = os.path.join(reportPath,lists[-1])
    return report_file

def send_email(sender, pwd, receiver,smt_server,report_file,port):
    """第四部，发送最新的测试报告内容"""
    with open(report_file, "rb") as f:
        mail_body = f.read()
    #定义邮件内容
    msg = MIMEMultipart()
    body = MIMEText(mail_body, _subtype="html", _charset="utf-8")
    msg['Subject'] = u"zentao自动化测试报告"
    msg['from'] = sender
    if isinstance(receiver, str):
        msg['to'] = receiver
    if isinstance(receiver, list):
        msg['to'] = ",".join(receiver)
    msg.attach(body)
    #添加附件
    att = MIMEText(open(report_file, "rb").read(), "base64", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment;filename= "report.html"'
    msg.attach(att)
    try:
        smtp = smtplib.SMTP()
        smtp.connect(smt_server)   #连接服务器
        smtp.login(sender.pwd)
    except:
        smtp = smtplib.SMTP_SSL(smt_server, port)
        smtp.login(sender, pwd)   #登录
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    print("test report email has send out")

if __name__ == "__main__":

    all_case = add_case() #加载用例
    run_case(all_case) #执行用例

    #获取最新测试报告文件
    report_path = os.path.join(current_path, "report") #用例文件夹
    report_file = get_report_file(report_path) #获取最新的测试报告

    #邮箱配置
    sender = "xxxxxxx@qq.com"
    pwd = "xxxxxxxxx"
    receiver = "xxxxx@qq.com"  #仅一个发送者/一个接受者
    #多个接受者：
    #receiver = ["1263872.com", "37287892.com", "62391qwwqw8.com"]
    smtp_server = "smtp.qq.com"
    port = 465

    # 发送报告
    send_email(sender, pwd, receiver, smtp_server, report_file, port)