from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = ""
TWITTER_PASSWORD = ""

chrome_driver_path = "C:/Users/Joseph/Documents/devbrowser/chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

class InternetSpeedTwitterBot:
    def __init__(self, driver):
        self.driver = driver
        self.up = 0
        self.down = 0
        
    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        sleep(10)
        speed_check = self.driver.find_element(By.CLASS_NAME, "js-start-test")
        sleep(60)
        down_speed=self.driver.find_element(By.CLASS_NAME,'download-speed').text
        print(down_speed)
        up_speed=self.driver.find_element(By.CLASS_NAME,'upload-speed').text
        print(up_speed)
        
    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")
        
        sleep(2)
        email = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input')
        password = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')

        email.send_keys(TWITTER_EMAIL)
        password.send_keys(TWITTER_PASSWORD)
        sleep(2)
        password.send_keys(Keys.ENTER)

        sleep(5)
        tweet_compose = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')

        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_compose.send_keys(tweet)
        sleep(3)

        tweet_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        tweet_button.click()

        sleep(2)
        self.driver.quit()
        
bot = InternetSpeedTwitterBot(driver)
bot.get_internet_speed()
bot.tweet_at_provider()