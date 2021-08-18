# CON_TC_1011_REG, CON_TC_1012_REG email address and password formal validity check
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import random
import string


def test_1011_reg():
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
        time.sleep(2)
        swal_text = driver.find_element_by_class_name("swal-text").text
        assert (swal_title == expected_title and swal_text == expected_text)

    def back_to_form():  # acknowledging error/getting sign up form back
        time.sleep(2)
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

    # check email without domain
    rnd_em_inv_1 = rnd_un + "@" + rnd_un
    user_registration(rnd_un, rnd_em_inv_1, rnd_pw)
    time.sleep(5)
    assert_handling("Registration failed!", "Email must be a valid email.")

    # check without @

    back_to_form()
    time.sleep(3)
    rnd_em_inv_2 = rnd_un + rnd_un + ".com"
    user_registration(rnd_un, rnd_em_inv_2, rnd_pw)
    time.sleep(3)
    assert_handling("Registration failed!", "Email must be a valid email.")
    back_to_form()

    #  password check 1: digit missing
    rnd_pw_inv1 = lowercase_part + uppercase_part + special_part
    user_registration(rnd_un, rnd_em, rnd_pw_inv1)
    time.sleep(3)
    assert_handling("Registration failed!", "Password must be 8 characters long and include 1 number, "
                                            "1 uppercase letter, and 1 lowercase letter.")
    back_to_form()
    time.sleep(3)

    # check 2: uppercase missing
    rnd_pw_inv2 = numeric_part + lowercase_part + special_part
    user_registration(rnd_un, rnd_em, rnd_pw_inv2)
    time.sleep(3)
    assert_handling("Registration failed!", "Password must be 8 characters long and include 1 number, "
                                            "1 uppercase letter, and 1 lowercase letter.")
    back_to_form()
    time.sleep(3)

    # check 3: lowercase missing
    rnd_pw_inv3 = numeric_part + uppercase_part + special_part
    user_registration(rnd_un, rnd_em, rnd_pw_inv3)
    time.sleep(3)
    assert_handling("Registration failed!", "Password must be 8 characters long and include 1 number, "
                                            "1 uppercase letter, and 1 lowercase letter.")
    back_to_form()

    # check 4: less than 8 chars
    lowercase_part_inv = "".join([random.choice(string.ascii_lowercase) for _ in range(2)])
    uppercase_part_inv = "".join([random.choice(string.ascii_uppercase) for _ in range(2)])
    rnd_pw_inv4 = lowercase_part_inv + uppercase_part_inv + numeric_part
    user_registration(rnd_un, rnd_em, rnd_pw_inv4)
    time.sleep(3)
    assert_handling("Registration failed!", "Password must be 8 characters long and include 1 number, "
                                            "1 uppercase letter, and 1 lowercase letter.")
    back_to_form()
    time.sleep(2)

    driver.close()
