from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

SECONDS_TO_WAIT = 15
PLAY_TIME = 60 * 5
chrome_driver_path = "C:/Users/Joseph/Documents/devbrowser/chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://orteil.dashnet.org/cookieclicker/")

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'English')]"))
)

language_picker = driver.find_element(By.XPATH, "//*[contains(text(), 'English')]")
language_picker.click()

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "bigCookie"))
)

cookie = driver.find_element(By.ID, "bigCookie")
timeout = time.time() + SECONDS_TO_WAIT
finish_time = time.time() + PLAY_TIME

while True:
    cookie = driver.find_element(By.ID, "bigCookie")
    cookie.click()
    current_time = time.time()
    if current_time > finish_time:
        break
    elif current_time > timeout:
        products = driver.find_elements(By.CLASS_NAME, "product")
        unlocked_enabled_products = [product for product in products if "unlocked enabled" in product.get_attribute("class")]

        if len(unlocked_enabled_products) > 0:
            unlocked_enabled_products[-1].click()
        timeout = time.time() + SECONDS_TO_WAIT
