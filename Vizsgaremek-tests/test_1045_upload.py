#  CON_TC_1045_UPLOAD, Repeated and sequenced data upload from data source

def test_1045_upload():
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    import csv
    import time
    from datetime import date
    from datetime import datetime

    # In order for ChromeDriverManager to work you must pip install it in your own environment.
    driver = webdriver.Chrome(ChromeDriverManager().install())

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

    def generate_article():
        new_article_link = driver.find_element_by_xpath("//*[@id='app']/nav/div/ul/li[2]/a")
        new_article_link.click()
        time.sleep(2)
        article_title = driver.find_element_by_xpath("//*[@id='app']//fieldset[1]/input")
        article_about = driver.find_element_by_xpath("//*[@id='app']//fieldset[2]/input")
        article_text = driver.find_element_by_xpath("//*[@id='app']//fieldset[3]/textarea")
        article_tag = driver.find_element_by_xpath("//*[@id='app']//fieldset[4]//input")
        publish_button = driver.find_element_by_xpath("//*[@id='app']//form/button")

        article_title.send_keys(row[0])
        article_about.send_keys(row[1])
        article_text.send_keys(row[2])
        article_tag.send_keys(row[3])
        time.sleep(2)
        publish_button.click()
        time.sleep(2)

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

            assert title == row[0]
            assert driver.current_url == "http://localhost:1667/#/articles/" + title.lower()
            assert author.is_displayed()
            assert author.text == user.text
            assert edit_article_btn.is_displayed() and edit_article_btn.is_enabled()
            assert del_article_btn.is_displayed() and del_article_btn.is_enabled()
            assert text == row[2]

            # date of creation validity

            today = date.today()
            article_date = driver.find_element_by_xpath("//span[@class='date']").text
            article_date_converted = datetime.strptime(article_date, "%B %d, %Y")
            date_to_set = datetime.date(article_date_converted)

            assert date_to_set == today







