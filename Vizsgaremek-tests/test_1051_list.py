#  CON_TC_1051_LIST Data listing

def test_1051_list():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
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

        # login to app
        driver.find_element_by_xpath("//*[@id='app']/nav/div/ul/li[2]/a").click()
        driver.find_element_by_xpath("//form/fieldset[1]/input").send_keys("testella@gmail.com")
        driver.find_element_by_xpath("//form/fieldset[2]/input").send_keys("Teszt123")
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/button').click()

        # listing articles with tag "dolor" from Popular Tags
        time.sleep(5)
        dolor_tag = driver.find_element_by_xpath("//*[ @id='app']/div/div[2]/div/div[2]/div/div/a[3]")
        dolor_tag.click()

        # validation of the list






    finally:
        pass


