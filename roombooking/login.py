import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from tempfile import mkdtemp

# Initialize the selenium webdriver
def initSelenium() -> webdriver.Chrome:
   chrome_options = Options()
   chrome_options.add_argument("--headless=new")
   chrome_options.add_argument("--no-sandbox")
   chrome_options.add_argument("--disable-dev-shm-usage")
   chrome_options.add_argument("--disable-gpu")
   chrome_options.add_argument("--disable-dev-tools")
   chrome_options.add_argument("--no-zygote")
   chrome_options.add_argument("--single-process")
   chrome_options.add_argument(f"--user-data-dir={mkdtemp()}")
   chrome_options.add_argument(f"--data-path={mkdtemp()}")
   chrome_options.add_argument(f"--disk-cache-dir={mkdtemp()}")
   chrome_options.add_argument("--remote-debugging-pipe")
   chrome_options.add_argument("--verbose")
   chrome_options.add_argument("--log-path=/tmp")
   chrome_options.binary_location = "/opt/chrome/chrome-linux64/chrome"

   service = Service(
      executable_path="/opt/chrome-driver/chromedriver-linux64/chromedriver",
      service_log_path="/tmp/chromedriver.log"
   )

   driver = webdriver.Chrome( 
      service=service,
      options=chrome_options
   )

   return driver


# Login to the Dal Killam booking system
def login(email: str, password: str, driver: webdriver.Chrome) -> webdriver.Chrome:
   driver.get('https://roombooking.library.dal.ca/')

   driver.maximize_window()

   email_field = driver.find_element(By.ID, 'email')
   password_field = driver.find_element(By.ID, 'password')

   email_field.send_keys(email)
   password_field.send_keys(password)

   time.sleep(1)

   login_button = driver.find_element(By.XPATH, '//button[@type="submit" and @name="login"]')
   login_button.click()
   print ("Logged in successfully")

   return driver


# Open a new tab of the booking page in the browser
def new_tab(driver: webdriver.Chrome, url: str) -> webdriver.Chrome:
   driver.execute_script("window.open('');")
   driver.switch_to.window(driver.window_handles[1])
   driver.get(url)
   print ("Opened new tab")
   return driver
