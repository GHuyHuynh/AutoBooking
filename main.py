import os
from dotenv import load_dotenv
from typing import List
from dates.date import limit_date_object
from roombooking.generate_url import generate_url
from roombooking.book_room import book_room

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

email = os.getenv('EMAIL')
password = os.getenv('PASSWORD')


result = book_room(email, password, url)

if result == 0:
   print("Room booked successfully!")

else:
   print("An error occurred while booking the room.")
   print('The error code is:', result)

