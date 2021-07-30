#  CON_TC_1045_DATA_MOD: data modification


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


def test_1045_data_mod():
    driver.get("http://localhost:1667")
    cookie_accept_button = driver.find_element_by_xpath("//div[@class='cookie__bar__buttons']/button[2]")
    cookie_accept_button.click()

    # login to app
    driver.find_element_by_xpath("//*[@id='app']/nav/div/ul/li[2]/a").click()
    driver.find_element_by_xpath("//form/fieldset[1]/input").send_keys("testella@gmail.com")
    driver.find_element_by_xpath("//form/fieldset[2]/input").send_keys("Teszt123")
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/button').click()
    time.sleep(2)
    # clicking on Settings link to modify data in Settings section

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='app']/nav/div/ul/li[3]/a")))
    driver.find_element_by_xpath("//*[@id='app']/nav/div/ul/li[3]/a").click()

    # modifying bio section, it already contains text
    entry = " I am an amazing tester."
    time.sleep(3)
    bio = driver.find_element_by_xpath("//*[@id='app']/div/div/div/div/form/fieldset/fieldset[3]/textarea")
    bio.clear()
    bio.send_keys(entry)
    update_button = driver.find_element_by_xpath("//button[@class='btn btn-lg btn-primary pull-xs-right']")
    update_button.click()
    time.sleep(3)
    swal_title = driver.find_element_by_class_name("swal-title")
    assert swal_title.text == "Update successful!"
    ok_button = driver.find_element_by_class_name("swal-button")
    ok_button.click()

    driver.close()
# az updatelt szoveget lehet-e ellenorizni?


