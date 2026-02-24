from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
url ="http://20.197.19.182:8080/"
def test_ui():

    options = Options()
    options.add_argument("--start-maximized")

    # Selenium Manager automatically finds ChromeDriver
    driver = webdriver.Chrome(options=options)

    driver.get(url)

    wait = WebDriverWait(driver, 10)

    name_box = wait.until(EC.presence_of_element_located((By.ID, "name")))
    time.sleep(2)
    name_box.send_keys("Dev")
    time.sleep(2)
    driver.find_element(By.TAG_NAME, "button").click()
    time.sleep(2)
    title_text = wait.until(EC.presence_of_element_located((By.ID, "title"))).text
    time.sleep(2)
    assert "Dev" in title_text


    driver.quit()





