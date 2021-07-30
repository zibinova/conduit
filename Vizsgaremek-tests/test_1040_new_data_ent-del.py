#  CON_TC_1040_NEW_DATA_ENT: new data entry


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


def test_1040_new_data_ent():
    try:
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
            EC.visibility_of_element_located((By.XPATH, "//*[@id='app']/div/div[2]/div[2]/div/div[1]/form/div[1]/textarea")))
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

        assert not driver.find_element_by_xpath("//div[@class='card']").text == comment

    finally:
        driver.close()
