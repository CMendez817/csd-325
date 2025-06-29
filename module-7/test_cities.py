# test_cities.py

import unittest
from city_functions import city_country  # Importing your function from city_functions.py

class CityCountryTestCase(unittest.TestCase):
    def test_city_country(self):
        """Test that city_country('santiago', 'chile') returns 'Santiago, Chile'."""
        result = city_country('santiago', 'chile')
        self.assertEqual(result, 'Santiago, Chile')

# This allows the test to run when the file is executed directly
if __name__ == '__main__':
    unittest.main()

# Keep the window open after running
input("\nPress Enter to exit...")