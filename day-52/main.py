from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep

SIMILAR_ACCOUNT = "mewtru"
USERNAME=""
PASSWORD=""

CHROME_DRIVER_PATH = "C:/Users/Joseph/Documents/devbrowser/chromedriver.exe"
service = Service(executable_path=CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service)

class InstaFollower:
    def __init__(self):
        self.driver = driver
        
    def login(self, username, password):
        self.username = username
        self.password = password
        self.driver.get("https://www.instagram.com/")
        sleep(3)
        user_name_input = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        user_name_input.send_keys(self.username)
        password_input = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_input.send_keys(self.password)
        sleep(3)
        login_button = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        sleep(5)
        login_button.click()
        sleep(10)
        not_now =self.driver.find_element(By.XPATH, '/*[@id="react-root"]/section/main/div/div/div/div/button')
        not_now.click()
        sleep(5)
        no_notifications = self.driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
        no_notifications.click()
        sleep(5)
        
        
    def find_followers(self):
        sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers/")
    
    def follow(self):
        self.driver.find_element(By.CSS_SELECTOR, 'ul a').click()
        sleep(6)
        follows = self.driver.find_elements_by_css_selector("._aano ._acan")
        i = 0
        for count in range(5):
            sleep(1)
            count += 1
            if i == 12:
                follows = self.driver.find_elements_by_css_selector("._aano ._acan")
            follows[i].location_once_scrolled_into_view
            try:
                follows[i].click()
            except ElementClickInterceptedException:
                self.driver.find_elements(By.CLASS_NAME, '_a9--')[1].click()
                sleep(2)
            i += 1
        
    
insta_bot = InstaFollower()

insta_bot.login(username=USERNAME, password=PASSWORD)
insta_bot.find_followers()
insta_bot.follow()