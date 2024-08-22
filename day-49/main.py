from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_driver_path = "C:/Users/Joseph/Documents/devbrowser/chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://www.linkedin.com/jobs/collections/recommended/?currentJobId=4003278095&discover=recommended&discoveryOrigin=JOBS_HOME_JYMBII&eBP=CwEAAAGReiJ-zOLTcLIScw-30A9Eunio26aRJvJwS7fBr8B_5gGcEW0bXbrw7nRnblnP9ZUZjNznWMIMdK-ITUTd-lYccoH3lTDe7N2SB7NUQ7WuyEHvtTQDrZl3MHE3PHkLy56X8giEU37-4whUJfo4BzbgQoSnhe3qJxM8Iot2kR9TLErs8U_Fftj8swKasP_jQ8jV0Jo-jKGIL8S_y6OtotbuM7V0MK5J0jWqSPdMobP8E3lmtBLWRF5QIyxek6F1hBeIZoXmJDZRsNC177lB2qUn4nyNxFKLXVnIzvyZXmz6nxc16XQp0zo8nX3mue9-k__39zYJF4FefoErA0Eja1P8S8ebWKn6rad_5AUqL-r5NLIxRkuRTc5XNvib-sHS_v0MmVPZms6qmMEJiffN3qJFUlRtrTbvlapANRjKJGva10uupb6tB-gZBCS_5vROU5zKsZZrHocDNkSHc_xHd8tBVnZy78C-hMqe&refId=wRpJc0ljCIJf%2F%2B%2FaVCYPfQ%3D%3D&trackingId=SYtKEM%2B3CYOevJTktl88cw%3D%3D")
# WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/header/nav/div/a[2]"))
# )

# driver.find_element(By.XPATH, '/html/body/div[1]/header/nav/div/a[2]').click()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="username"]'))
)

email_input = driver.find_element(By.XPATH, '//*[@id="username"]')
email_input.send_keys("cjkinuthia5@gmail.com")

password_input = driver.find_element(By.XPATH, '//*[@id="password"]')
password_input.send_keys("kinuthia@01")

sign_in = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button').click()

jobs_list = driver.find_elements(By.CSS_SELECTOR, ".jobs-search-results__list-item")

def apply_jobs():
    apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-apply-button").click()
    #unfinished, can't apply

for job in jobs_list:
    job.click()
    apply_jobs()
    time.sleep(10)



time.sleep(20)