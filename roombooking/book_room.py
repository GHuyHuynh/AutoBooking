from roombooking import login
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def book_room(email: str, password: str, url: str) -> int:
   driver = login.initSelenium()
   driver = login.login(email, password, driver)
   driver = login.new_tab(driver, url)

   time.sleep(1)

   title_field = driver.find_element(By.ID, 'reservation-title')
   reminder_checkbox = driver.find_element(By.ID, 'start-reminder-enabled')
   description_field = driver.find_element(By.ID, 'reservation-description')
   phone_field = driver.find_element(By.ID, 'attribute-2')
   terms_checkbox = driver.find_element(By.ID, 'reservation-terms-checkbox')

   title_field.send_keys('Project Meeting')
   reminder_checkbox.click()
   description_field.send_keys('Project details')
   phone_field.send_keys('902-545-2239')

   terms_checkbox.click()

   submit_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div[2]/button')
   
   WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div[2]/button')))

   driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)

   time.sleep(1)
   submit_button.click()

   time.sleep(1)

   driver.quit()
   print("Driver quit")

   return 0  # Success
