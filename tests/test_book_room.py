import unittest
from unittest.mock import patch, MagicMock
from roombooking.book_room import book_room
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class TestBookRoom(unittest.TestCase):
    @patch('roombooking.book_room.login.initSelenium')
    @patch('roombooking.book_room.login.login')
    @patch('roombooking.book_room.login.new_tab')
    @patch('roombooking.book_room.time.sleep')
    @patch('roombooking.book_room.WebDriverWait')
    def test_book_room(self, mock_wait, mock_sleep, mock_new_tab, mock_login, mock_init_selenium):
        # Create mock driver and elements
        mock_driver = MagicMock()
        mock_title_field = MagicMock()
        mock_reminder_checkbox = MagicMock()
        mock_description_field = MagicMock()
        mock_phone_field = MagicMock()
        mock_terms_checkbox = MagicMock()
        mock_submit_button = MagicMock()
        mock_wait_instance = MagicMock()
        
        # Set up the driver's find_element method to return our mocks
        mock_driver.find_element.side_effect = lambda by, value: {
            (By.ID, 'reservation-title'): mock_title_field,
            (By.ID, 'start-reminder-enabled'): mock_reminder_checkbox,
            (By.ID, 'reservation-description'): mock_description_field,
            (By.ID, 'attribute-2'): mock_phone_field,
            (By.ID, 'reservation-terms-checkbox'): mock_terms_checkbox,
            (By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div[2]/button'): mock_submit_button
        }[(by, value)]
        
        # Set up the mocks for the login module functions
        mock_init_selenium.return_value = mock_driver
        mock_login.return_value = mock_driver
        mock_new_tab.return_value = mock_driver
        
        # Set up the WebDriverWait mock
        mock_wait.return_value = mock_wait_instance
        mock_wait_instance.until.return_value = mock_submit_button
        
        # Call the book_room function
        result = book_room("test@example.com", "password123", "https://example.com/booking")
        
        # Verify the login module functions were called correctly
        mock_init_selenium.assert_called_once()
        mock_login.assert_called_once_with("test@example.com", "password123", mock_driver)
        mock_new_tab.assert_called_once_with(mock_driver, "https://example.com/booking")
        
        # Verify sleep was called
        mock_sleep.assert_called()
        
        # Verify the form fields were filled out
        mock_title_field.send_keys.assert_called_once_with('Project Meeting')
        mock_reminder_checkbox.click.assert_called_once()
        mock_description_field.send_keys.assert_called_once_with('Project details')
        mock_phone_field.send_keys.assert_called_once_with('902-545-2239')
        mock_terms_checkbox.click.assert_called_once()
        
        # Verify WebDriverWait was used for the submit button
        mock_wait.assert_called_once_with(mock_driver, 1)
        
        # Verify the submit button was clicked
        mock_driver.execute_script.assert_called_with("arguments[0].scrollIntoView(true);", mock_submit_button)
        mock_submit_button.click.assert_called_once()
        
        # Verify the driver was quit
        mock_driver.quit.assert_called_once()
        
        # Verify the function returns 0 (success)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main() 