# CON_TC_1023_LOG User login to Conduit happy path

def test_1023_log():

    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    import time

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
            time.sleep(2)
            sign_in_button.click()

        def assert_handling(expected_title, expected_text):
            swal_title = driver.find_element_by_class_name("swal-title").text
            swal_text = driver.find_element_by_class_name("swal-text").text
            assert (swal_title == expected_title and swal_text == expected_text)

        def back_to_form():  # acknowledging error/getting sign up form back
            ok_button = driver.find_element_by_class_name("swal-button")
            ok_button.click()

        user_login("testella@gmail.com", "Teszt123")
        time.sleep(2)
        user = driver.find_element_by_xpath("//*[@id='app']/nav/div/ul/li[4]/a")
        assert user.is_displayed()
        assert user.text == "testella"

    finally:
        driver.close()
























