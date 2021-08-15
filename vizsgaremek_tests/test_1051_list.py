#  CON_TC_1051_LIST: Data listing

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time


def test_1051_list():

    options = Options()
    options.headless = True
    # driver = webdriver.Chrome(ChromeDriverManager().install())
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)  # headless mode

    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')

    driver.get("http://localhost:1667")
    cookie_accept_button = driver.find_element_by_xpath("//div[@class='cookie__bar__buttons']/button[2]")
    cookie_accept_button.click()

    def login():
        driver.find_element_by_xpath("//*[@id='app']/nav/div/ul/li[2]/a").click()
        driver.find_element_by_xpath("//form/fieldset[1]/input").send_keys("testella@gmail.com")
        driver.find_element_by_xpath("//form/fieldset[2]/input").send_keys("Teszt123")
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/button').click()
        time.sleep(5)

    login()

    # listing articles with tag "dolor" from Popular Tags section
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[ @id='app']/div/div[2]/div/div[2]/div/div/a[3]")))
    dolor_pop_tag = driver.find_element_by_xpath("//*[ @id='app']/div/div[2]/div/div[2]/div/div/a[3]")
    dolor_pop_tag.click()

    # validation of the list
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='app']/div/div[2]/div/div[1]/div[1]/ul/li[3]/a")))
    dolor_feed = driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div/div[1]/div[1]/ul/li[3]/a")
    assert dolor_feed.is_displayed()
    assert dolor_feed.text == "dolor"

    dolor_list = driver.find_elements_by_xpath("//div[@class='article-preview']")
    assert len(dolor_list) == 16

    # checking if all articles has the dolor tag
    dolor_tags = driver.find_elements_by_xpath("//div[@class='article-preview']/a/div/a[@href='#/tag/dolor']")
    assert len(dolor_tags) == len(dolor_list)

    driver.close()
    driver.quit()


