from datetime import datetime, timedelta
from typing import List

# Constants
HOURS_1: List[int] = [9, 11]
HOURS_2: List[int] = [11, 13]
HOURS_3: List[int] = [13, 15]
HOURS_4: List[int] = [15, 17]

# Reference URL
# Room 1 Wallace McCain Learning Commons
# rid refers to room id (room 4 = 17)
# sid refers to space id (wallace mccain learning commons = 14)

base_url: str = 'https://roombooking.library.dal.ca/reservation/?rid=17&sid=14&rd=2025-02-03&sd=2025-02-03%2009%3A00%3A00&ed=2025-02-03%2011%3A00%3A00'

# Template URL to insert params
template_url: str = 'https://roombooking.library.dal.ca/reservation/?rid={rid}&sid={sid}&rd={year}-{month}-{day}&sd={year}-{month}-{day}%20{start_hour}%3A00%3A00&ed={year}-{month}-{day}%20{end_hour}%3A00%3A00'


def generate_url(date: str, month: str, year: str, start_hour: int, end_hour: int) -> str:
   rid: int = 17
   sid: int = 14
   
   return template_url.format(rid=rid, sid=sid, year=year, month=month, day=date, start_hour=start_hour, end_hour=end_hour)


# Run the test
if __name__ == '__main__':
   date: datetime = datetime.now() + timedelta(days=2)
   today_day: str = date.strftime('%d')
   today_month: str = date.strftime('%m')
   today_year: str = date.strftime('%Y')

   # Book room at 2days away date from 9am to 11am
   booking_url = generate_url(today_day, today_month, today_year, 9, 11)
   print(booking_url)

