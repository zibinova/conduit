#  CON_TC_1010_REG-1013_REG, User registration to Conduit app

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import random
import string

options = Options()
options.headless = True

# driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)  # headless mode

# options.add_argument('--headless')
# options.add_argument('--disable-gpu')

driver.get("http://localhost:1667")

# giving cookie consent
cookie_accept_button = driver.find_element_by_xpath("//div[@class='cookie__bar__buttons']/button[2]")
cookie_accept_button.click()


def user_registration(username, email, password):
    user_name = driver.find_element_by_xpath("//form/fieldset[1]/input")
    e_mail = driver.find_element_by_xpath("//form/fieldset[2]/input")
    pass_word = driver.find_element_by_xpath("//form/fieldset[3]/input")
    sign_up_button = driver.find_element_by_xpath('//form/button')

    user_name.send_keys(username)
    e_mail.send_keys(email)
    pass_word.send_keys(password)
    time.sleep(3)
    sign_up_button.click()


def assert_handling(expected_title, expected_text):

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@class='swal-title']")))

    swal_title = driver.find_element_by_xpath("//div[@class='swal-title']").text
    swal_text = driver.find_element_by_class_name("swal-text").text
    assert (swal_title == expected_title and swal_text == expected_text)


def back_to_form():  # acknowledging error/getting sign up form back
    ok_button = driver.find_element_by_class_name("swal-button")
    ok_button.click()


# generating random test data

numeric_part = "".join([random.choice(string.digits) for _ in range(2)])
lowercase_part = "".join([random.choice(string.ascii_lowercase) for _ in range(4)])
uppercase_part = "".join([random.choice(string.ascii_uppercase) for _ in range(4)])
special_part = "".join([random.choice(string.punctuation) for _ in range(2)])
rnd_un = "".join([random.choice(string.ascii_lowercase) for _ in range(5)])
rnd_em = rnd_un + "@" + lowercase_part + ".com"
rnd_pw = numeric_part + lowercase_part + uppercase_part + special_part


# getting sign-up form

sign_up_link = driver.find_element_by_xpath("//ul/li[3]/a")
sign_up_link.click()
time.sleep(3)

# registration attempts with missing data/blank form validation:


def test_1010_reg():

    user_registration("", "", "")
    time.sleep(3)
    assert_handling("Registration failed!", "Username field required.")
    back_to_form()
    time.sleep(3)

# missing email and password

    user_registration(rnd_un, "", "")
    time.sleep(3)
    assert_handling("Registration failed!", "Email field required.")
    back_to_form()

# missing password

    user_registration(rnd_un, rnd_em, "")
    time.sleep(3)
    assert_handling("Registration failed!", "Password field required.")


# CON_TC_1013_REG happy path successful user reg.

def test_1013_reg():
    back_to_form()
    time.sleep(2)
    user_registration(rnd_un, rnd_em, rnd_pw)
    time.sleep(5)
    assert_handling("Welcome!", "Your registration was successful!")
    back_to_form()
    time.sleep(2)
    user = driver.find_element_by_xpath("//*[@id='app']/nav/div/ul/li[4]/a")
    assert user.is_displayed()
    assert user.text == rnd_un

