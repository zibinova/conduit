#  CON_TC_1041_UPLOAD, Repeated and sequenced data upload from data source

def test_1041_upload():

    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.chrome.options import Options
    import csv
    import time
    from datetime import date
    from datetime import datetime

    options = Options()
    options.headless = True
    # In order for ChromeDriverManager to work you must pip install it in your own environment.

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
    driver.find_element_by_xpath("//*[@id='app']/nav/div/ul/li[2]/a").click()
    driver.find_element_by_xpath("//form/fieldset[1]/input").send_keys("testella@gmail.com")
    driver.find_element_by_xpath("//form/fieldset[2]/input").send_keys("Teszt123")
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/button').click()
    time.sleep(2)

    # check current number of "My articles"

    user = driver.find_element_by_xpath("//*[@id='app']/nav/div/ul/li[4]/a")
    user.click()
    article_list = driver.find_elements_by_class_name("article-preview")
    print(len(article_list))

    def generate_article():
        new_article_link = driver.find_element_by_xpath("//*[@id='app']/nav/div/ul/li[2]/a")
        new_article_link.click()
        time.sleep(1)
        article_title = driver.find_element_by_xpath("//*[@id='app']//fieldset[1]/input")
        article_about = driver.find_element_by_xpath("//*[@id='app']//fieldset[2]/input")
        article_text = driver.find_element_by_xpath("//*[@id='app']//fieldset[3]/textarea")
        article_tag = driver.find_element_by_xpath("//*[@id='app']//fieldset[4]//input")
        publish_button = driver.find_element_by_xpath("//*[@id='app']//form/button")

        article_title.send_keys(row[0])
        article_about.send_keys(row[1])
        article_text.send_keys(row[2])
        article_tag.send_keys(row[3])
        time.sleep(1)
        publish_button.click()
        time.sleep(1)

    with open("new_article.csv", encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        next(reader)
        for row in reader:

            generate_article()

            title = driver.find_element_by_tag_name("h1").text
            user = driver.find_element_by_xpath("//*[@id='app']/nav/div/ul/li[4]/a")
            author = driver.find_element_by_class_name("author")
            edit_article_btn = driver.find_element_by_xpath("//span/a")
            del_article_btn = driver.find_element_by_xpath("//span/button")
            text = driver.find_element_by_xpath("//p").text
            tag = driver.find_element_by_xpath("//div[@class='tag-list']/a").text

            assert title == row[0]
            assert driver.current_url == "http://localhost:1667/#/articles/" + title.lower()
            assert author.is_displayed()
            assert author.text == user.text
            assert edit_article_btn.is_displayed() and edit_article_btn.is_enabled()
            assert del_article_btn.is_displayed() and del_article_btn.is_enabled()
            assert text == row[2]
            assert tag == row[3]

            # date of creation validity

            today = date.today()
            article_date = driver.find_element_by_xpath("//span[@class='date']").text
            article_date_converted = datetime.strptime(article_date, "%B %d, %Y")
            date_to_set = datetime.date(article_date_converted)

            assert date_to_set == today

    # check if newly created blogs have been added to "My articles"
    # considering that pagination is not working correctly, all articles would appear on page 1

    user.click()
    time.sleep(1)
    assert driver.current_url == "http://localhost:1667/#/@" + user.text + "/"

    # determine number of rows in csv

    file = open("new_article.csv")
    reader = csv.reader(file)
    next(reader)
    rows = len(list(reader))

    # check the current article numbers:
    new_article_list = driver.find_elements_by_class_name("article-preview")
    assert (len(article_list) + rows) == len(new_article_list)

    # itt szeretnem osszehasonlítani a csv title listat a selected /vagyis ujonnan letrehozott/
    # article title listaval: de még küzdök

    # with open("new_article.csv") as csv_file:
    #     reader = csv.reader(csv_file, delimiter=',')
    #     next(reader)
    #     for row in reader:
    #         exp_titles = ("".join(row[0]))
    #         print(exp_titles)
    #
    # titles = driver.find_elements_by_tag_name("h1")
    # selected_titles = titles[-rows:]
    # print(selected_titles)
    # assert exp_titles == selected_titles







