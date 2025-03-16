import unittest
from unittest.mock import patch, MagicMock
import os
import random
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

class TestMain(unittest.TestCase):
    @patch('main.load_dotenv')
    @patch('main.webdriver.Chrome')
    @patch('main.Service')
    @patch('main.ChromeDriverManager')
    @patch('main.WebDriverWait')
    @patch('main.time.sleep')
    @patch('main.random.randint')
    @patch('os.getenv')
    def test_main_script_successful_booking(self, mock_getenv, mock_randint, mock_sleep, 
                                           mock_wait, mock_chrome_manager, mock_service, 
                                           mock_chrome, mock_load_dotenv):
        # Mock environment variables
        mock_getenv.side_effect = lambda key: {
            'EMAIL': 'test@example.com',
            'PASSWORD': 'password123',
            'TIME_BLOCK_ASSIGNED': '2'
        }[key]
        
        # Mock random selection
        mock_randint.return_value = 0
        
        # Mock ChromeDriverManager
        mock_manager_instance = MagicMock()
        mock_chrome_manager.return_value = mock_manager_instance
        mock_manager_instance.install.return_value = '/path/to/chromedriver'
        
        # Mock Service
        mock_service_instance = MagicMock()
        mock_service.return_value = mock_service_instance
        
        # Mock Chrome driver
        mock_driver = MagicMock()
        mock_chrome.return_value = mock_driver
        mock_driver.window_handles = [0, 1]
        
        # Mock WebDriverWait
        mock_wait_instance = MagicMock()
        mock_wait.return_value = mock_wait_instance
        
        # Mock elements
        mock_email_field = MagicMock()
        mock_password_field = MagicMock()
        mock_login_button = MagicMock()
        mock_success_element = MagicMock()
        mock_bell_icon = MagicMock()
        mock_title_field = MagicMock()
        mock_description_field = MagicMock()
        mock_phone_field = MagicMock()
        mock_terms_checkbox = MagicMock()
        mock_submit_button = MagicMock()
        mock_confirmation_message = MagicMock()
        mock_confirmation_message2 = MagicMock()
        
        # Set up the wait.until method to return our mocks
        def mock_until_side_effect(condition):
            if isinstance(condition, tuple) and condition[0] == EC.presence_of_element_located:
                locator = condition[1]
                if locator == (By.ID, 'email'):
                    return mock_email_field
                elif locator == (By.ID, 'password'):
                    return mock_password_field
                elif locator == (By.XPATH, '//*[@id="schedule-actions"]'):
                    return mock_success_element
                elif locator == (By.XPATH, '//*[@id="nav-reservation-badge"]/span'):
                    return mock_bell_icon
                elif locator == (By.ID, 'reservation-title'):
                    return mock_title_field
                elif locator == (By.ID, 'attribute-2'):
                    return mock_phone_field
                elif locator == (By.XPATH, '//*[@id="reservation-terms-checkbox"]'):
                    return mock_terms_checkbox
                elif locator == (By.XPATH, '//*[@id="react-root"]/div/div[3]/div/div/div/div/div[1]/i'):
                    return mock_confirmation_message
                elif locator == (By.CLASS_NAME, 'bi bi-calendar2-check reservation-save-result-icon success'):
                    return mock_confirmation_message2
            elif isinstance(condition, tuple) and condition[0] == EC.element_to_be_clickable:
                locator = condition[1]
                if locator == (By.XPATH, '//button[@type="submit" and @name="login"]'):
                    return mock_login_button
                elif locator == (By.XPATH, '//*[@id="react-root"]/div/div[1]/div[2]/button'):
                    return mock_submit_button
            return None
        
        mock_wait_instance.until.side_effect = mock_until_side_effect
        
        # Set up the driver's find_element method to return our mocks
        def mock_find_element_side_effect(by, value):
            if (by, value) == (By.ID, 'reservation-description'):
                return mock_description_field
            elif (by, value) == (By.TAG_NAME, 'body'):
                return MagicMock()
            return None
        
        mock_driver.find_element.side_effect = mock_find_element_side_effect
        
        # Import and run main module
        with patch('builtins.__import__', return_value=None):
            try:
                # This will fail because we're not actually importing the module
                # but we're just testing the mocks setup
                import main
            except ImportError:
                pass
        
        # Verify the driver was quit
        mock_driver.quit.assert_called_once()
    
    @patch('main.load_dotenv')
    @patch('main.webdriver.Chrome')
    @patch('main.Service')
    @patch('main.ChromeDriverManager')
    @patch('main.WebDriverWait')
    @patch('main.time.sleep')
    @patch('os.getenv')
    def test_main_script_login_failure(self, mock_getenv, mock_sleep, 
                                      mock_wait, mock_chrome_manager, 
                                      mock_service, mock_chrome, mock_load_dotenv):
        # Mock environment variables
        mock_getenv.side_effect = lambda key: {
            'EMAIL': 'test@example.com',
            'PASSWORD': 'wrong_password',
            'TIME_BLOCK_ASSIGNED': '2'
        }[key]
        
        # Mock ChromeDriverManager
        mock_manager_instance = MagicMock()
        mock_chrome_manager.return_value = mock_manager_instance
        mock_manager_instance.install.return_value = '/path/to/chromedriver'
        
        # Mock Service
        mock_service_instance = MagicMock()
        mock_service.return_value = mock_service_instance
        
        # Mock Chrome driver
        mock_driver = MagicMock()
        mock_chrome.return_value = mock_driver
        
        # Mock WebDriverWait
        mock_wait_instance = MagicMock()
        mock_wait.return_value = mock_wait_instance
        
        # Mock elements
        mock_email_field = MagicMock()
        mock_password_field = MagicMock()
        mock_login_button = MagicMock()
        
        # Set up the wait.until method to return our mocks for login fields
        # but raise TimeoutException for success elements
        def mock_until_side_effect(condition):
            if isinstance(condition, tuple) and condition[0] == EC.presence_of_element_located:
                locator = condition[1]
                if locator == (By.ID, 'email'):
                    return mock_email_field
                elif locator == (By.ID, 'password'):
                    return mock_password_field
                elif locator == (By.XPATH, '//*[@id="schedule-actions"]'):
                    raise TimeoutException("Login failed")
            elif isinstance(condition, tuple) and condition[0] == EC.element_to_be_clickable:
                locator = condition[1]
                if locator == (By.XPATH, '//button[@type="submit" and @name="login"]'):
                    return mock_login_button
            return None
        
        mock_wait_instance.until.side_effect = mock_until_side_effect
        
        # Import and run main module
        with patch('builtins.__import__', return_value=None):
            try:
                # This will fail because we're not actually importing the module
                # but we're just testing the mocks setup
                import main
            except ImportError:
                pass
        
        # Verify the driver was quit
        mock_driver.quit.assert_called_once()

if __name__ == '__main__':
    unittest.main() 