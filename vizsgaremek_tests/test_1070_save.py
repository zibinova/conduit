# CON_TC_1070_SAVE: Saving data to csv file

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time


def test_1070_save():
    options = Options()
    options.headless = True

    # driver = webdriver.Chrome(ChromeDriverManager().install())
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)  # headless mode

    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')

    URL = "http://localhost:1667"
    driver.get(URL)

    # cookie handling
    cookie_accept_button = driver.find_element_by_xpath("//div[@class='cookie__bar__buttons']/button[2]")
    cookie_accept_button.click()

    # login to app

    def login():
        driver.find_element_by_xpath("//*[@id='app']/nav/div/ul/li[2]/a").click()
        driver.find_element_by_xpath("//form/fieldset[1]/input").send_keys("testella@gmail.com")
        driver.find_element_by_xpath("//form/fieldset[2]/input").send_keys("Teszt123")
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/button').click()
        time.sleep(5)

    login()
    time.sleep(5)

    articles = driver.find_elements_by_xpath('//div[@class="article-preview"]')
    print(len(articles))

    articles_number = 0
    with open("articles.txt", "w", encoding="utf-8") as file:
        for article in articles:
            file.write(f"{article.text}")
            articles_number += 1

    with open("articles.txt", "r", encoding="utf-8") as file:
        result = file.readlines()
        print(result)

        assert result[3] == "Lorem ipsum dolor sit amet\n"

    assert len(articles) == articles_number
    driver.close()
