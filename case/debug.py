import time
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://127.0.0.1:81/zentao/user-login.html")
driver.find_element_by_id("account").send_keys("admin")
driver.find_element_by_name("password").send_keys("hyl@qq.com")
driver.find_element_by_id("submit").click()
driver.get("http://127.0.0.1:81/zentao/bug-create-1-0-moduleID=0.html")
time.sleep(3)
driver.find_element_by_xpath("//*[@id='submit']").click()