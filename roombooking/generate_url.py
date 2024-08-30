from datetime import datetime, timedelta
from typing import List

# Constants
HOURS_1: List[int] = [9, 11]
HOURS_2: List[int] = [11, 13]
HOURS_3: List[int] = [13, 15]
HOURS_4: List[int] = [15, 17]

# Reference URL
base_url: str = 'https://roombooking.library.dal.ca/reservation/?rid=208&sid=16&rd=2024-08-15&sd=2024-08-15%2012%3A00%3A00&ed=2024-08-15%2014%3A00%3A00'

# Template URL to insert params
template_url: str = 'https://roombooking.library.dal.ca/reservation/?rid=378&sid=16&rd={year}-{month}-{day}&sd={year}-{month}-{day}%20{start_hour}%3A00%3A00&ed={year}-{month}-{day}%20{end_hour}%3A00%3A00'



def generate_url(date: str, month: str, year: str, start_hour: int, end_hour: int) -> str:
   return template_url.format(year=year, month=month, day=date, start_hour=start_hour, end_hour=end_hour)


# Run the test
if __name__ == '__main__':
   date: datetime = datetime.now() + timedelta(days=2)
   today_day: str = date.strftime('%d')
   today_month: str = date.strftime('%m')
   today_year: str = date.strftime('%Y')

   # Book room at 2days away date from 9am to 11am
   booking_url = generate_url(today_day, today_month, today_year, 9, 11)
   print(booking_url)

