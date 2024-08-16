import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# Initialize the selenium webdriver
def initSelenium() -> webdriver.Chrome:
   driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
   return driver


# Login to the Dal Killam booking system
def login(email: str, password: str, driver: webdriver.Chrome) -> webdriver.Chrome:
   driver.get('https://roombooking.library.dal.ca/')


   email_field = driver.find_element(By.ID, 'email')
   password_field = driver.find_element(By.ID, 'password')

   email_field.send_keys(email)
   password_field.send_keys(password)

   time.sleep(1)

   login_button = driver.find_element(By.XPATH, '//button[@type="submit" and @name="login"]')
   login_button.click()

   return driver


# Open a new tab of the booking page in the browser
def new_tab(driver: webdriver.Chrome, url: str) -> webdriver.Chrome:
   driver.execute_script("window.open('');")
   driver.switch_to.window(driver.window_handles[1])
   driver.get(url)
   return driver
