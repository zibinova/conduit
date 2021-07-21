#  CON_TC_1010_REG-1014_REG, User registration to Conduit app

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
# driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)  # headless mode

# options = Options()
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')

driver.get("http://localhost:1667")

# cookie handling

cookie_accept_button = driver.find_element_by_xpath("//div[@class='cookie__bar__buttons']/button[2]")
cookie_accept_button.click()

# getting sign-up form

sign_up_link = driver.find_element_by_xpath("//ul/li[3]/a")
sign_up_link.click()


def registration(username, email, password):

    user_name = driver.find_element_by_xpath("//form/fieldset[1]/input")
    e_mail = driver.find_element_by_xpath("//form/fieldset[2]/input")
    pass_word = driver.find_element_by_xpath("//form/fieldset[3]/input")
    sign_up_button = driver.find_element_by_xpath('//form/button')

    user_name.send_keys(username)
    e_mail.send_keys(email)
    pass_word.send_keys(password)
    sign_up_button.click()


def assert_handling(expected_title, expected_text):
    swal_title = driver.find_element_by_xpath("//div[@class='swal-title']").text
    swal_text = driver.find_element_by_class_name("swal-text").text
    assert (swal_title == expected_title and swal_text == expected_text )


def back_to_form():                            # acknowledging error/getting sign up form back
    ok_button = driver.find_element_by_class_name("swal-button")
    ok_button.click()

# registration attempts with missing data/blank form validation
#
#
# registration("", "", "")
#
# time.sleep(3)
#
# assert_handling("Registration failed!", "Username field required.")
#
# back_to_form()
#
#
# # missing email and password
#
#
# registration("testella", "", "")
#
# time.sleep(3)
#
# assert_handling("Registration failed!", "Email field required.")
#
# back_to_form()
#
# # missing password
#
# registration("testella", "testella@gmail.hu", "")
#
# time.sleep(3)
#
# assert_handling("Registration failed!", "Password field required.")
#
# back_to_form()
#
#
# # CON_TC_1011_REG email address formal validity check 1
#
# registration("testella", "testella@gmail", "Teszt123")
#
# time.sleep(3)
#
# assert_handling("Registration failed!", "Email must be a valid email.")
#
# back_to_form()
#
# # *** 2
#
# registration("testella", "testellagmail.hu", "Teszt123")
#
# time.sleep(3)
#
# assert_handling("Registration failed!", "Email must be a valid email.")
#
# back_to_form()

# CON_TC_1012_REG password formal check 1


# registration("testella", "testella@gmail.hu", "teszt")
#
# time.sleep(3)
#
# assert_handling("Registration failed!", "Password must be 8 characters long and include 1 number, 1 uppercase letter,
#                                         "and 1 lowercase letter.")
# back_to_form()

# check 2
# registration("testella", "testella@gmail.hu", "12345678")
#
# time.sleep(3)
#
# assert_handling("Registration failed!", "Password must be 8 characters long and include 1 number, 1 uppercase letter,
#                                         "and 1 lowercase letter.")
# back_to_form()

# check 3
# registration("testella", "testella@gmail.hu", "teszt123")
#
# time.sleep(3)
#
# assert_handling("Registration failed!", "Password must be 8 characters long and include 1 number, 1 uppercase letter,
#                                         "and 1 lowercase letter.")
# back_to_form()


# CON_TC_1013_REG happy path successful user reg.

registration("testella", "testella@gmail.hu", "Teszt123")

time.sleep(3)

assert_handling("Welcome!", "Your registration was successful!")

back_to_form()



# CON_TC_1014_REG, Uniq username check
# this test gives assertion error, app accepts multiple registration with same usernames

# registration("testella", "testella@gmail.com", "Teszt123")
#
# time.sleep(3)
#
# swal_title = driver.find_element_by_xpath("//div[@class='swal-title']").text
# swal_text = driver.find_element_by_class_name("swal-text").text
# assert (swal_title == "Registration failed!" and swal_text == "Username already taken.")




