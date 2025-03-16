import unittest
from unittest.mock import patch
from datetime import datetime, timedelta
from dates.date import limit_date_object

class TestDate(unittest.TestCase):
    @patch('dates.date.datetime')
    def test_limit_date_calculation(self, mock_datetime):
        # Mock the current date to a fixed value
        mock_now = datetime(2023, 5, 15)
        mock_datetime.now.return_value = mock_now
        
        # Mock the date limit (7 days from now)
        mock_limit = mock_now + timedelta(days=7)
        
        # Import the module again to use our mocked datetime
        import importlib
        import dates.date
        importlib.reload(dates.date)
        
        # Check if limit_date_object has the correct values
        expected_day = mock_limit.strftime('%d')
        expected_month = mock_limit.strftime('%m')
        expected_year = mock_limit.strftime('%Y')
        
        self.assertEqual(dates.date.limit_date_object['day'], expected_day)
        self.assertEqual(dates.date.limit_date_object['month'], expected_month)
        self.assertEqual(dates.date.limit_date_object['year'], expected_year)

if __name__ == '__main__':
    unittest.main() 