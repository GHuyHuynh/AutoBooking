from killam import generate_url
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from datetime import datetime
from typing import List

from killam.generate_url import generate_url
from dates.date import limit_date_object

# Constants
HOURS_1: List[int] = [9, 11]
HOURS_2: List[int] = [11, 13]
HOURS_3: List[int] = [13, 15]
HOURS_4: List[int] = [15, 17]


day: str = limit_date_object['day']
month: str = limit_date_object['month']
year: str = limit_date_object['year']

url = generate_url(day, month, year, HOURS_1[0], HOURS_1[1])


# Set up the Chrome driver
chrome_options = Options()




