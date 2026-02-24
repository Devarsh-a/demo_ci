from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_ui():

    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Selenium Manager automatically finds ChromeDriver
    driver = webdriver.Chrome(options=options)

    driver.get("http://localhost:3000")

    wait = WebDriverWait(driver, 10)

    name_box = wait.until(EC.presence_of_element_located((By.ID, "name")))
    name_box.send_keys("Dev")

    driver.find_element(By.TAG_NAME, "button").click()

    title_text = wait.until(EC.presence_of_element_located((By.ID, "title"))).text

    assert "Dev" in title_text

    driver.quit()