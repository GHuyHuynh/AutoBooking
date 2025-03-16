import unittest
import sys
import os

# Add the parent directory to the path so we can import the modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import all test modules
from tests.test_date import TestDate
from tests.test_generate_url import TestGenerateUrl
from tests.test_login import TestLogin
from tests.test_book_room import TestBookRoom
from tests.test_main import TestMain

# Create a test suite
def create_test_suite():
    test_suite = unittest.TestSuite()
    
    # Add test cases
    test_suite.addTest(unittest.makeSuite(TestDate))
    test_suite.addTest(unittest.makeSuite(TestGenerateUrl))
    test_suite.addTest(unittest.makeSuite(TestLogin))
    test_suite.addTest(unittest.makeSuite(TestBookRoom))
    test_suite.addTest(unittest.makeSuite(TestMain))
    
    return test_suite

if __name__ == '__main__':
    # Create the test suite
    suite = create_test_suite()
    
    # Run the tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Return non-zero exit code if tests failed
    sys.exit(not result.wasSuccessful()) 