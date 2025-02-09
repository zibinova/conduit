# CON_TC_1014_REG, 1015_REG Sign-up with account/username already existing
# 1015 expected to fail, app allows using multiple username

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import random
import string


def test_reg_1014_15():
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

    user_registration("testella", "testella@gmail.com", "Teszt123")
    time.sleep(5)
    assert_handling("Registration failed!", "Email already taken.")

    # CON_TC_1015_REG, Sign-up with not yet registered email but already existing username
    # this test expected to give assertion error, since app accepts multiple registration with same usernames

    back_to_form()
    time.sleep(2)
    rnd_em1 = lowercase_part + "@" + lowercase_part + ".com"
    user_registration("testella", rnd_em1, rnd_pw)
    time.sleep(5)
    assert_handling("Registration failed!", "Username already taken.")
    driver.close()
