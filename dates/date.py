from datetime import datetime, timedelta
from typing import Dict

# Dal Killam booking system allow for booking up to 7 days in advance

# Can avoid weekend if needed with CRON configuration on AWS

date: datetime = datetime.now()

# Run on max possible date to book
date_limit: datetime = datetime.now() + timedelta(days=7)

today_day: str = date.strftime('%d')
limit_day: str = date_limit.strftime('%d')

today_month: str = date.strftime('%m')
limit_month: str = date_limit.strftime('%m')

today_year: str = date.strftime('%Y')
limit_year: str = date_limit.strftime('%Y')

limit_date_object: Dict[str, str] = {
   'day': limit_day,
   'month': limit_month,
   'year': limit_year,
}

