from selenium import webdriver

def loginFunction(driver,user="admin",pwd="hyl@qq.com"):
    driver = webdriver.Firefox()
    driver.get("http://127.0.0.1:81/zentao/user-login.html")
    driver.find_element_by_id("account").send_keys(user)
    driver.find_element_by_name("password").send_keys(pwd)
    driver.find_element_by_id("submit").click()
