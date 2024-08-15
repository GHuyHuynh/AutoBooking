import datetime
from typing import List


# Constants
HOURS_1: List[int] = [9, 11]
HOURS_2: List[int] = [11, 13]
HOURS_3: List[int] = [13, 15]
HOURS_4: List[int] = [15, 17]


base_url: str = 'https://roombooking.library.dal.ca/reservation/?rid=208&sid=16&rd=2024-08-15&sd=2024-08-15%2012%3A00%3A00&ed=2024-08-15%2014%3A00%3A00'

template_url: str = 'https://roombooking.library.dal.ca/reservation/?rid=208&sid=16&rd={year}-{month}-{day}&sd={year}-{month}-{day}%20{start_hour}%3A00%3A00&ed={year}-{month}-{day}%20{end_hour}%3A00%3A00'

# Dal Killam booking system allow for booking up to 7 days in advance
# Right the code book 6 days in advance

# TODO: Add function to exclude weekends if needed

date: datetime.datetime = datetime.datetime.now()

date_limit: datetime = datetime.datetime.now() + datetime.timedelta(days=7)

today_date: str = date.strftime('%d')
limit_date: str = date_limit.strftime('%d')

today_month: str = date.strftime('%m')
limit_month: str = date_limit.strftime('%m')

today_year: str = date.strftime('%Y')
limit_year: str = date_limit.strftime('%Y')


def generate_url(date: str, month: str, year: str, start_hour: int, end_hour: int) -> str:
   return template_url.format(year=year, month=month, day=date, start_hour=start_hour, end_hour=end_hour)


def generate_1_limi_booking_url(hours: List[int]) -> str:
   return generate_url(limit_date, limit_month, limit_year, hours[0], hours[1])


# Run the test
if __name__ == '__main__':
   booking = generate_1_limi_booking_url(HOURS_1) 
   print(booking)
