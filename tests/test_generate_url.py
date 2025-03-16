import unittest
from roombooking.generate_url import generate_url

class TestGenerateUrl(unittest.TestCase):
    def test_generate_url_format(self):
        # Test with sample data
        day = "15"
        month = "05"
        year = "2023"
        start_hour = 9
        end_hour = 11
        
        expected_url = "https://roombooking.library.dal.ca/reservation/?rid=17&sid=14&rd=2023-05-15&sd=2023-05-15%2009%3A00%3A00&ed=2023-05-15%2011%3A00%3A00"
        
        # Generate the URL
        result_url = generate_url(day, month, year, start_hour, end_hour)
        
        # Check if the generated URL matches the expected format
        self.assertEqual(result_url, expected_url)
    
    def test_generate_url_different_times(self):
        # Test with different time slots
        day = "20"
        month = "06"
        year = "2023"
        
        # Test morning slot
        morning_url = generate_url(day, month, year, 9, 11)
        expected_morning = "https://roombooking.library.dal.ca/reservation/?rid=17&sid=14&rd=2023-06-20&sd=2023-06-20%2009%3A00%3A00&ed=2023-06-20%2011%3A00%3A00"
        self.assertEqual(morning_url, expected_morning)
        
        # Test afternoon slot
        afternoon_url = generate_url(day, month, year, 13, 15)
        expected_afternoon = "https://roombooking.library.dal.ca/reservation/?rid=17&sid=14&rd=2023-06-20&sd=2023-06-20%2013%3A00%3A00&ed=2023-06-20%2015%3A00%3A00"
        self.assertEqual(afternoon_url, expected_afternoon)
        
        # Test evening slot
        evening_url = generate_url(day, month, year, 19, 21)
        expected_evening = "https://roombooking.library.dal.ca/reservation/?rid=17&sid=14&rd=2023-06-20&sd=2023-06-20%2019%3A00%3A00&ed=2023-06-20%2021%3A00%3A00"
        self.assertEqual(evening_url, expected_evening)

if __name__ == '__main__':
    unittest.main() 