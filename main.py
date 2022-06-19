from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://lms.umt.edu.pk/login/index.php")
driver.find_element_by_id("username").send_keys('F2019105109')
driver.find_element_by_id("password").send_keys('gKkTn5@X')
driver.find_element_by_id('loginbtn').click()

m=driver.find_elements_by_tag_name("a")

for x in range(17,24):

        print(m[x].text)
