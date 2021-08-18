# CON_TC_1024_LOG User logout of Conduit app

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time


def test_1024_logout():
    options = Options()
    options.headless = True

    # driver = webdriver.Chrome(ChromeDriverManager().install())
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)  # headless mode

    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')

    driver.get("http://localhost:1667")

    sign_in_link = driver.find_element_by_xpath("//*[@id='app']/nav/div/ul/li[2]/a")
    sign_in_link.click()
    time.sleep(2)

    def user_login(email, password):
        e_mail = driver.find_element_by_xpath("//form/fieldset[1]/input")
        pass_word = driver.find_element_by_xpath("//form/fieldset[2]/input")
        sign_in_button = driver.find_element_by_xpath('//form/button')

        e_mail.send_keys(email)
        pass_word.send_keys(password)
        sign_in_button.click()

    user_login("testella@gmail.com", "Teszt123")
    time.sleep(2)

    # perform logout

    logout = driver.find_element_by_xpath("//*[@id='app']/nav/div/ul/li[5]/a")
    logout.click()
    time.sleep(2)
    assert sign_in_link.is_displayed()
    sign_up_link = driver.find_element_by_xpath("//ul/li[3]/a")
    assert sign_up_link.is_displayed()

    driver.close()
