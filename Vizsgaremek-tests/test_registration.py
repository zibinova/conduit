# CON_TC_1010_REG
# User registration to Conduit app, registration test with missing data

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

import time
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("http://localhost:1667")

cookie_accept_button = driver.find_element_by_xpath("//div[@class='cookie__bar__buttons']/button[2]")

cookie_accept_button.click()

# if cookie_button
# cookie_button.click()

sign_up_link = driver.find_element_by_xpath("//ul/li[3]/a")
sign_up_link.click()

sign_up_button = driver.find_element_by_xpath("//form/button")
sign_up_button.click()

time.sleep(3)

swal_title = driver.find_element_by_class_name("swal-title").text
swal_text = driver.find_element_by_class_name("swal-text").text
assert (swal_title == "Registration failed!" and swal_text == "Username field required.")


ok_button = driver.find_element_by_class_name("swal-button")
ok_button.click()








# username = driver.find_element_by_xpath("//form/fieldset[1]/input")
# username.send_keys("")



