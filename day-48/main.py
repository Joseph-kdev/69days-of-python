from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_driver_path = "C:/Users/Joseph/Documents/devbrowser/chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

# WebDriverWait(driver, 15).until(
#     EC.presence_of_element_located((By.ID, "APjFqb"))
# )

# driver.get("https://google.com")           
# input_element  = driver.find_element(By.ID, "APjFqb")
# input_element.send_keys("Internet" + Keys.ENTER)

# link = driver.find_element(By.PARTIAL_LINK_TEXT, "The Internet")
# link.click()

# search_bar = driver.find_element(By.NAME, "q")
# search_bar.send_keys("list", Keys.ENTER)

# submit = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(submit.text)

driver.get("https://www.python.org/")
# list_elements = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[1]')
event_dict = {}

for i in range(0, 5):
    list_element = driver.find_element(By.XPATH, f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{i}]').text
    list_date = list_element.split("\n")[0]
    list_name = list_element.split("\n")[1]
    event_dict[i] = {
        list_date: list_name
    }

print(event_dict)

time.sleep(10)



