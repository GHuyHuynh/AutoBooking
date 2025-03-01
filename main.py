import os
import random
from dotenv import load_dotenv
from typing import List
from dates.date import limit_date_object
from roombooking.generate_url import generate_url
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from constants.constants import title_arrays, description_arrays

load_dotenv()

# Constants
HOURS_0: List[int] = [9, 11]
HOURS_1: List[int] = [11, 13]
HOURS_2: List[int] = [13, 15]
HOURS_3: List[int] = [15, 17]
HOURS_4: List[int] = [17, 19]
HOURS_5: List[int] = [19, 21]

TIME_BLOCKS: List[List[int]] = [HOURS_0, HOURS_1, HOURS_2, HOURS_3, HOURS_4, HOURS_5]


day: str = limit_date_object['day']
month: str = limit_date_object['month']
year: str = limit_date_object['year']


email:str = os.getenv('EMAIL')
password: str = os.getenv('PASSWORD')
time_block_assigned: int = int(os.getenv('TIME_BLOCK_ASSIGNED'))

personal_time_block: List[int] = TIME_BLOCKS[time_block_assigned]


# Randomly select title and description
random_index_title = random.randint(0, len(title_arrays) - 1)
random_index_desc = random.randint(0, len(description_arrays) - 1)
title_input: str = title_arrays[random_index_title]
description_input: str = description_arrays[random_index_desc]


chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')

service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service, options=chrome_options)

# Login

url = 'https://roombooking.library.dal.ca/'
login_url = generate_url(day, month, year, personal_time_block[0], personal_time_block[1])
print(login_url)

driver.get(url)

time.sleep(2)

email_field = WebDriverWait(driver, 1).until(
   EC.presence_of_element_located((By.ID, 'email'))
)
email_field.send_keys(email)

password_field = WebDriverWait(driver, 1).until(
   EC.presence_of_element_located((By.ID, 'password'))
)
password_field.send_keys(password)

print("Email and password entered successfully")

login_button = WebDriverWait(driver, 1).until(
   EC.element_to_be_clickable((By.XPATH, '//button[@type="submit" and @name="login"]'))
)

driver.execute_script("arguments[0].scrollIntoView(true);", login_button)
driver.execute_script("arguments[0].click();", login_button)

try:
   success_element = WebDriverWait(driver,1).until(
      EC.presence_of_element_located((By.XPATH, '//*[@id="schedule-actions"]'))  
   )

   bell_icon = WebDriverWait(driver, 1).until(
      EC.presence_of_element_located((By.XPATH, '//*[@id="nav-reservation-badge"]/span'))
   )
                                      
   print("Logged in successfully")
except TimeoutException:
   print("Login failed")


# Book a room
print("Start room booking")
driver.execute_script("window.open('');")

driver.switch_to.window(driver.window_handles[1])

driver.get(login_url)
print(login_url)

# Wait for the page to load completely
try:
   WebDriverWait(driver, 60).until(
      lambda driver: driver.execute_script('return document.readyState') == 'complete'
   )
   print("Booking Page loaded successfully after 60 sec webdriver wait")
except TimeoutException:
   print("Page failed to load completely after 60 seconds")


try:
   title_field = WebDriverWait(driver, 30).until(
      EC.presence_of_element_located((By.ID, 'reservation-title'))
   )
   print("Found reservation title field")
except TimeoutException:
   print("Could not find reservation title field, trying one more time")

   # 2nd attempt
   try:
      title_field = WebDriverWait(driver, 30).until(
         EC.presence_of_element_located((By.ID, 'reservation-title'))
      )
      print("Found reservation title field after second attempt")
   except TimeoutException:
      print("Could not find reservation title field after second attempt")


title_field.send_keys(title_input)

# reminder_checkbox = driver.find_element(By.ID, 'start-reminder-enabled')
description_field = driver.find_element(By.ID, 'reservation-description')
description_field.send_keys(description_input)

time.sleep(1)

try:
   print("Trying to find phone field")
   phone_field = WebDriverWait(driver, 1).until(
      EC.visibility_of_element_located((By.ID, 'attribute-2'))
   )
   
   driver.execute_script("arguments[0].scrollIntoView(true);", phone_field)
   
   WebDriverWait(driver, 1).until(
      EC.element_to_be_clickable((By.ID, 'attribute-2'))
   )
   
   phone_field.send_keys('5062559845')
   print("Phone field found and entered")

   body = driver.find_element(By.TAG_NAME, 'body')
   body.click()
   print("Clicked away from phone field")
   time.sleep(1)

except TimeoutException:
   print("Phone field not found")


time.sleep(1)

terms_checkbox = WebDriverWait(driver, 1).until(
   EC.presence_of_element_located((By.XPATH, '//*[@id="reservation-terms-checkbox"]'))
)                                   

driver.execute_script("arguments[0].scrollIntoView(true);", terms_checkbox)
driver.execute_script("arguments[0].click();", terms_checkbox)

time.sleep(2)

submit_button = WebDriverWait(driver, 1).until(
   EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/div/div[1]/div[2]/button'))
)

driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
driver.execute_script("arguments[0].click();", submit_button)

print("Executed submit button")

time.sleep(1)

try:
   confirmation_message = WebDriverWait(driver, 1).until(
      EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div[3]/div/div/div/div/div[1]/i'))  
   )

   confirmation_message2 = WebDriverWait(driver, 1).until(
      EC.presence_of_element_located((By.CLASS_NAME, 'bi bi-calendar2-check reservation-save-result-icon success'))  
   )
   
   print("Room booked successfully")
   
# TODO: fix this error message block, sometimes successful booking message is display inside the error block
except TimeoutException:
   print("Room booking failed")
   error_message = WebDriverWait(driver, 1).until(
      EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div[3]/div/div/div'))  
   )
   print(error_message.text)
   inner_html = error_message.get_attribute('innerHTML')
   print(inner_html)


driver.quit()


