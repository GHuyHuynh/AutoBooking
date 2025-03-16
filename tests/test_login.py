import unittest
from unittest.mock import patch, MagicMock
from roombooking.login import initSelenium, login, new_tab

class TestLogin(unittest.TestCase):
    @patch('roombooking.login.webdriver.Chrome')
    @patch('roombooking.login.Service')
    @patch('roombooking.login.Options')
    @patch('roombooking.login.mkdtemp')
    def test_init_selenium(self, mock_mkdtemp, mock_options, mock_service, mock_chrome):
        # Mock the temporary directory creation
        mock_mkdtemp.side_effect = ['/tmp/dir1', '/tmp/dir2', '/tmp/dir3']
        
        # Mock the Chrome options
        mock_options_instance = MagicMock()
        mock_options.return_value = mock_options_instance
        
        # Mock the Service
        mock_service_instance = MagicMock()
        mock_service.return_value = mock_service_instance
        
        # Mock the Chrome driver
        mock_driver = MagicMock()
        mock_chrome.return_value = mock_driver
        
        # Call the function
        result = initSelenium()
        
        # Verify Chrome options were set correctly
        self.assertEqual(mock_options_instance.add_argument.call_count, 14)
        mock_options_instance.add_argument.assert_any_call("--headless=new")
        mock_options_instance.add_argument.assert_any_call("--no-sandbox")
        mock_options_instance.add_argument.assert_any_call("--disable-dev-shm-usage")
        
        # Verify Service was created with correct parameters
        mock_service.assert_called_once_with(
            executable_path="/opt/chrome-driver/chromedriver-linux64/chromedriver",
            service_log_path="/tmp/chromedriver.log"
        )
        
        # Verify Chrome was initialized with correct parameters
        mock_chrome.assert_called_once_with(
            service=mock_service_instance,
            options=mock_options_instance
        )
        
        # Verify the function returns the Chrome driver
        self.assertEqual(result, mock_driver)
    
    @patch('roombooking.login.time.sleep')
    def test_login_function(self, mock_sleep):
        # Create mock driver and elements
        mock_driver = MagicMock()
        mock_email_field = MagicMock()
        mock_password_field = MagicMock()
        mock_login_button = MagicMock()
        
        # Set up the driver's find_element method to return our mocks
        mock_driver.find_element.side_effect = lambda by, value: {
            ('id', 'email'): mock_email_field,
            ('id', 'password'): mock_password_field,
            ('xpath', '//button[@type="submit" and @name="login"]'): mock_login_button
        }[(by, value)]
        
        # Call the login function
        result = login("test@example.com", "password123", mock_driver)
        
        # Verify the driver navigated to the correct URL
        mock_driver.get.assert_called_once_with('https://roombooking.library.dal.ca/')
        
        # Verify the window was maximized
        mock_driver.maximize_window.assert_called_once()
        
        # Verify the email and password were entered
        mock_email_field.send_keys.assert_called_once_with("test@example.com")
        mock_password_field.send_keys.assert_called_once_with("password123")
        
        # Verify sleep was called
        mock_sleep.assert_called_once_with(1)
        
        # Verify the login button was clicked
        mock_login_button.click.assert_called_once()
        
        # Verify the function returns the driver
        self.assertEqual(result, mock_driver)
    
    def test_new_tab(self):
        # Create mock driver
        mock_driver = MagicMock()
        mock_driver.window_handles = [0, 1]
        
        # Call the new_tab function
        result = new_tab(mock_driver, "https://example.com")
        
        # Verify a new window was opened
        mock_driver.execute_script.assert_called_once_with("window.open('');")
        
        # Verify the driver switched to the new window
        mock_driver.switch_to.window.assert_called_once_with(1)
        
        # Verify the driver navigated to the correct URL
        mock_driver.get.assert_called_once_with("https://example.com")
        
        # Verify the function returns the driver
        self.assertEqual(result, mock_driver)

if __name__ == '__main__':
    unittest.main() 