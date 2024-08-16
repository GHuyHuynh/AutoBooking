from roombooking import login
import os
from dotenv import load_dotenv

load_dotenv()

test_email = os.environ['TEST_EMAIL']
test_password = os.environ['TEST_PASSWORD']

def test_login():
   driver = login.initSelenium()
   email = test_email
   password = test_password
   driver = login.login(email, password, driver)
   # Booking page, if logged in correctly
   # Should appear the room G40I
   url_1 = 'https://roombooking.library.dal.ca/reservation/?rid=208&sid=16&rd=2024-08-15&sd=2024-08-15%2011%3A00%3A00&ed=2024-08-15%2013%3A00%3A00'
   driver = login.new_tab(driver, url_1)

# Run the test
if __name__ == '__main__':
   test_login()   