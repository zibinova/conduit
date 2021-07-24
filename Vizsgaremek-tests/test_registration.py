#  CON_TC_1000_REG-1014_REG, User registration to Conduit app

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import string

driver = webdriver.Chrome(ChromeDriverManager().install())
# driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)  # headless mode

# options = Options()
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')

driver.get("http://localhost:1667")


# CON_TC_1000_REG giving cookie policy consent and check:


def test_reg_1000():
    assert driver.find_element_by_id('cookie-policy-panel').is_displayed()
    cookie_accept_button = driver.find_element_by_xpath("//div[@class='cookie__bar__buttons']/button[2]")
    cookie_accept_button.click()


# getting sign-up form


sign_up_link = driver.find_element_by_xpath("//ul/li[3]/a")
sign_up_link.click()


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


# registration attempts with missing data/blank form validation:


def test_reg_1010():

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
    back_to_form()

#  CON_TC_1011_REG email address formal validity check (1)


def test_reg_1011():

    rnd_em_inv_1 = rnd_un + "@" + rnd_un
    user_registration(rnd_un, rnd_em_inv_1, rnd_pw)
    time.sleep(3)
    assert_handling("Registration failed!", "Email must be a valid email.")
    back_to_form()
    time.sleep(3)

    #  *** check 2

    rnd_em_inv_2 = rnd_un + rnd_un + ".com"
    user_registration(rnd_un, rnd_em_inv_2, rnd_pw)
    assert_handling("Registration failed!", "Email must be a valid email.")
    back_to_form()

# # CON_TC_1012_REG password formal check


def test_reg_1012():
    #  check 1: digit missing
    rnd_pw_inv1 = lowercase_part + uppercase_part + special_part
    user_registration(rnd_un, rnd_em, rnd_pw_inv1)
    time.sleep(3)
    assert_handling("Registration failed!", "Password must be 8 characters long and include 1 number, "
                                            "1 uppercase letter, and 1 lowercase letter.")
    back_to_form()
    time.sleep(3)

    # check 2 uppercase missing
    rnd_pw_inv2 = numeric_part + lowercase_part + special_part
    user_registration(rnd_un, rnd_em, rnd_pw_inv2)
    time.sleep(3)
    assert_handling("Registration failed!", "Password must be 8 characters long and include 1 number, "
                                            "1 uppercase letter, and 1 lowercase letter.")
    back_to_form()
    time.sleep(3)

    # check 3 lowercase missing
    rnd_pw_inv3 = numeric_part + uppercase_part + special_part
    user_registration(rnd_un, rnd_em, rnd_pw_inv3)
    time.sleep(3)
    assert_handling("Registration failed!", "Password must be 8 characters long and include 1 number, "
                                            "1 uppercase letter, and 1 lowercase letter.")
    back_to_form()

    # check 4 less than 8 chars
    lowercase_part_inv = "".join([random.choice(string.ascii_lowercase) for _ in range(2)])
    uppercase_part_inv = "".join([random.choice(string.ascii_uppercase) for _ in range(2)])
    rnd_pw_inv4 = lowercase_part_inv + uppercase_part_inv + numeric_part
    user_registration(rnd_un, rnd_em, rnd_pw_inv4)
    time.sleep(3)
    assert_handling("Registration failed!", "Password must be 8 characters long and include 1 number, "
                                            "1 uppercase letter, and 1 lowercase letter.")
    back_to_form()

# CON_TC_1013_REG happy path successful user reg.


def test_reg_1013():
    user_registration(rnd_un, rnd_em, rnd_pw)
    time.sleep(2)
    assert_handling("Welcome!", "Your registration was successful!")
    back_to_form()
    user = driver.find_element_by_xpath("//*[@id='app']/nav/div/ul/li[4]/a")
    assert user.is_displayed()
    assert user.text == rnd_un
    time.sleep(2)

    # perform logout
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='app']/nav/div/ul/li[5]/a"))).click()
    time.sleep(3)


# CON_TC_1014_REG, Sign-up with account already existing


def test_reg_1014():
    # getting sign-up form
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//ul/li[3]/a"))).click()
    time.sleep(5)
    user_registration("testella", "testella@gmail.com", "Teszt123")
    time.sleep(5)
    assert_handling("Registration failed!", "Email already taken.")


# CON_TC_1015_REG, Sign-up with not yet registered email but already existing username
# this test gives assertion error, app accepts multiple registration with same usernames/or not accepting valid email


def test_reg_1015():
    back_to_form()
    user_registration("testella", rnd_em, rnd_pw)
    time.sleep(5)
    assert_handling("Registration failed!", "Username already taken.")
