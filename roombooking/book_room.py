from typing import List
from roombooking.generate_url import generate_url
from dates.date import limit_date_object
from roombooking import login
import os
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
import time

load_dotenv()

# Constants
HOURS_1: List[int] = [9, 11]
HOURS_2: List[int] = [11, 13]
HOURS_3: List[int] = [13, 15]
HOURS_4: List[int] = [15, 17]


day: str = limit_date_object['day']
month: str = limit_date_object['month']
year: str = limit_date_object['year']

url = generate_url(day, month, year, HOURS_2[0], HOURS_2[1])


def book_room():
   driver = login.initSelenium()
   email = os.environ['TEST_EMAIL']
   password = os.environ['TEST_PASSWORD']
   driver = login.login(email, password, driver)
   driver = login.new_tab(driver, url)

   time.sleep(2)

   title_field = driver.find_element(By.ID, 'reservation-title')
   reminder_checkbox = driver.find_element(By.ID, 'start-reminder-enabled')
   description_field = driver.find_element(By.ID, 'reservation-description')
   phone_field = driver.find_element(By.ID, 'attribute-2')
   terms_checkbox = driver.find_element(By.ID, 'reservation-terms-checkbox')
   submit_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div[2]/button')

   title_field.send_keys('Summer Project')
   reminder_checkbox.click()
   description_field.send_keys('Summer project work')
   phone_field.send_keys('902-502-4554')
   terms_checkbox.click()

   time.sleep(1)

   submit_button.click()

if __name__ == '__main__':
   book_room()


