#  CON_TC_1000_policy cookie consent giving check
def test_reg_1000():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from webdriver_manager.chrome import ChromeDriverManager
    import time
    from selenium.common.exceptions import NoSuchElementException

    driver = webdriver.Chrome(ChromeDriverManager().install())
    # driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)  # headless mode

    # options = Options()
    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')

    try:
        driver.get("http://localhost:1667")
        time.sleep(5)
        assert driver.find_element_by_id('cookie-policy-panel').is_displayed()
        cookie_accept_button = driver.find_element_by_xpath("//div[@class='cookie__bar__buttons']/button[2]")
        cookie_accept_button.click()

        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "driver.find_element_by_id('cookie-policy-panel')")))
            not_found = False

        except:
            not_found = True
        assert not_found

        driver.refresh()
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "driver.find_element_by_id('cookie-policy-panel')")))
            not_found = False

        except:
            not_found = True
        assert not_found

    finally:
        driver.close()
