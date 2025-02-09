#  CON_TC_1040_ENTRY_DEL: new data entry and deletion
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time


def test_1040_entry_del():
    options = Options()
    options.headless = True

    # driver = webdriver.Chrome(ChromeDriverManager().install())
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)  # headless mode

    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')

    driver.get("http://localhost:1667")
    cookie_accept_button = driver.find_element_by_xpath("//div[@class='cookie__bar__buttons']/button[2]")
    cookie_accept_button.click()

    # login to app
    driver.find_element_by_xpath("//*[@id='app']/nav/div/ul/li[2]/a").click()
    driver.find_element_by_xpath("//form/fieldset[1]/input").send_keys("testella@gmail.com")
    driver.find_element_by_xpath("//form/fieldset[2]/input").send_keys("Teszt123")
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/button').click()

    # click on a chosen blog:
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id ='app']/div/div[2]/div/div[1]/div[2]/div/div/div[1]/a")))
    driver.find_element_by_xpath("//*[@id ='app']/div/div[2]/div/div[1]/div[2]/div/div/div[1]/a").click()

    # click on comment area:
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//*[@id='app']/div/div[2]/div[2]/div/div[1]/form/div[1]/textarea")))
    driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[2]/div/div[1]/form/div[1]/textarea").click()

    comment = "I like this article"
    driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[2]/div/div[1]/form/div[1]/textarea").send_keys(comment)

    post_button = driver.find_element_by_xpath("//div[@class='card-footer']/button")
    post_button.click()

    time.sleep(2)
    assert driver.find_element_by_xpath("//div[@class='card']/div/p").text == comment

    # delete comment:
    trash_icon = driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[2]/div/div[2]/div[2]/span[2]/i")
    trash_icon.click()
    time.sleep(5)

    assert not len(driver.find_elements_by_xpath("//div[@class='card']"))

    driver.close()
