# CON_TC_1021_LOG User login to Conduit app, missing login data check
# ez a  teszt elbukik pedig nem kene, manualisan jol lefut,
# a missing password resznel nem a megfelelo hibauzit adja

def test_1021_log():

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

    try:

        driver.get("http://localhost:1667")

        cookie_accept_button = driver.find_element_by_xpath("//div[@class='cookie__bar__buttons']/button[2]")
        cookie_accept_button.click()

        sign_in_link = driver.find_element_by_xpath("//*[@id='app']/nav/div/ul/li[2]/a")
        sign_in_link.click()
        time.sleep(2)

        def user_login(email, password):

            e_mail = driver.find_element_by_xpath("//form/fieldset[1]/input")
            pass_word = driver.find_element_by_xpath("//form/fieldset[2]/input")
            sign_in_button = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/button')

            e_mail.clear()
            pass_word.clear()
            e_mail.send_keys(email)
            pass_word.send_keys(password)
            time.sleep(3)
            sign_in_button.click()

        def assert_handling(expected_title, expected_text):
            swal_title = driver.find_element_by_class_name("swal-title").text
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

        # blank input fields

        user_login("", "")
        time.sleep(2)
        assert_handling("Login failed!", "Email field required.")
        time.sleep(2)
        back_to_form()

        # missing password

        time.sleep(3)
        user_login(rnd_em, "")
        time.sleep(3)
        assert_handling("Login failed!", "Password field required.")

    finally:
        driver.close()















