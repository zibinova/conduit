#  CON_TC_1000_policy cookie consent giving check

def test_1000_policy():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from webdriver_manager.chrome import ChromeDriverManager
    import time
    from selenium.common.exceptions import NoSuchElementException
    import pytest

    driver = webdriver.Chrome(ChromeDriverManager().install())
    # driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)  # headless mode

    # options = Options()
    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')

    driver.get("http://localhost:1667")
    time.sleep(2)
    assert driver.find_element_by_id('cookie-policy-panel').is_displayed()
    time.sleep(2)
    cookie_accept_button = driver.find_element_by_xpath("//div[@class='cookie__bar__buttons']/button[2]")
    cookie_accept_button.click()

    # checking if panel has disappeared:
    assert not len(driver.find_elements_by_id('cookie-policy-panel'))






