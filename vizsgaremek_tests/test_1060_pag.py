# CON_TC_1060_PAG : Pagination test in global feed
# expected to fail since app displays same articles on multiple pages,
# throws the last couple of articles per page to the following page

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time


def test_1060_pag():
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

    assert driver.current_url == "http://localhost:1667/#/"

    assert driver.find_element_by_class_name("pagination").is_displayed()
    pages = driver.find_elements_by_class_name("page-link")

    # pagination:

    article_title_list = []
    for page in pages:
        time.sleep(2)
        page.click()
        time.sleep(2)
        article_titles = driver.find_elements_by_xpath('//div[@class="article-preview"]//h1')
        for article in article_titles:
            article_title_list.append(article.text)

    print("Number of articles in Global feed: ", len(article_title_list))
    print("Global feed's article list: \n", "\n".join(article_title_list))

    assert len(article_title_list) == 22

    # checking if pagination works in terms of no duplicate articles on different pages of the feed
    # fails

    page2_article_titles = driver.find_elements_by_xpath('//div[@class="article-preview"]//h1')
    page2_article_title_list = []
    for article in page2_article_titles:
        page2_article_title_list.append(article.text)
    print(page2_article_title_list)
    assert not any(item in article_title_list for item in page2_article_title_list)

    driver.close()
