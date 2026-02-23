from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

options = Options()
options.binary_location="/usr/bin/chromium"
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=Service("/usr/bin/chromedriver"), options=options)

driver.get("http://localhost:3000")
time.sleep(1)

driver.find_element(By.ID,"name").send_keys("Dev")
driver.find_element(By.TAG_NAME,"button").click()

time.sleep(1)
text = driver.find_element(By.ID,"title").text

assert "Dev" in text

driver.quit()