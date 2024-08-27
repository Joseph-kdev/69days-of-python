from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_driver_path = "C:/Users/Joseph/Documents/devbrowser/chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://tinder.com")

cookies = driver.find_element(By.XPATH,"//*[text()='I decline']")
cookies.click()
time.sleep(2)
login = driver.find_element(By.XPATH,"//*[text()='Log in']")
login.click()
time.sleep(10)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="container"]')))
facebook = driver.find_element(By.XPATH,"//*[text()='Login with Facebook']")
facebook.click()
time.sleep(2)
driver.switch_to.window(driver.window_handles[1])
time.sleep(2)
facebookCookies = driver.find_element(By.XPATH,"//*[@data-cookiebanner='accept_only_essential_button']")
facebookCookies.click()
time.sleep(2)
email = driver.find_element(By.XPATH,"//*[@id='email']")
email.send_keys(EMAIL)
password = driver.find_element(By.XPATH,"//*[@id='pass']")
password.send_keys(PASSWORD+Keys.ENTER)
time.sleep(10)
driver.switch_to.window(driver.window_handles[0])
location = driver.find_element(By.XPATH,"//*[text()='Allow']")
location.click()
time.sleep(2)
notifications = driver.find_element(By.XPATH,"//*[text()='Not interested']")
notifications.click()
time.sleep(5)