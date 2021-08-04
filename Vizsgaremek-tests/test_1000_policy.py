#  CON_TC_1000_policy cookie consent giving check, test fails as cookie has been accepted,
#  panel still appears after reopening the page
# at manual test working fine...

def test_1000_policy():
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.chrome.options import Options
    import time

    options = Options()
    options.headless = True

    # driver = webdriver.Chrome(ChromeDriverManager().install())
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)  # headless mode

    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')

    driver.get("http://localhost:1667")
    time.sleep(2)
    assert driver.find_element_by_id('cookie-policy-panel').is_displayed()
    time.sleep(2)
    cookie_accept_button = driver.find_element_by_xpath("//div[@class='cookie__bar__buttons']/button[2]")
    cookie_accept_button.click()
    time.sleep(2)
    # checking if panel has disappeared:This should pass assertion if
    # none of elements that match your locator were found
    # or AssertionError if at least 1 found
    assert not len(driver.find_elements_by_id('cookie-policy-panel'))

    driver.close()

    # reopen browser
    import time
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.chrome.options import Options

    options = Options()
    options.headless = True
    # In order for ChromeDriverManager to work you must pip install it in your own environment.
    # driver = webdriver.Chrome(ChromeDriverManager().install())
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)  # headless mode

    URL = "http://localhost:1667"
    driver.get(URL)
    time.sleep(3)

    assert not driver.find_element_by_id('cookie-policy-panel').is_displayed()

    driver.close()




