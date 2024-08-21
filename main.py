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


def lambda_handler(event, context):
   day: str = limit_date_object['day']
   month: str = limit_date_object['month']
   year: str = limit_date_object['year']

   url: str = generate_url(day, month, year, HOURS_2[0], HOURS_2[1])

   email: str = os.getenv('EMAIL')
   password: str = os.getenv('PASSWORD')

   result: int = book_room(email, password, url)

   if result == 0:
      return {
         'statusCode': 200,
         'body': 'Room booked successfully!'
      }
   
   else:
      return {
         'statusCode': 500,
         'body': f'An error occurred while booking the room. Error code: {result}'
      }

