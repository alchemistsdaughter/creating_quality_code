import a1
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """

    # Add your test methods for a1.stock_price_summary here.
    def test_stock_example_1(self):
        """Test price_changes with mixed list of changes including zeros."""
		
        actual = stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
        expected = (0.14, -0.17)
        self.assertAlmostEqual(expected, actual, places = 10, msg = None, delta = None)
        
    def test_stock_example_2(self):
        """Test price_changes with an empty list."""
		
        actual = stock_price_summary([])
        expected = (0.0, 0.0)
        self.assertAlmostEqual(expected, actual, places = 10, msg = None, delta = None)
        
    def test_stock_example_3(self):
        """Test price_changes with only negative numbers."""
		
        actual = stock_price_summary([-2, -0.01, -.9])
        expected = (0.0, -2.91)
        self.assertAlmostEqual(expected, actual, places = 10, msg = None, delta = None)
        
    def test_stock_example_3(self):
        """Test price_changes with only positive numbers."""
		
        actual = stock_price_summary([2, 0.01, .9, 0])
        expected = (2.91, 0.0)
        self.assertAlmostEqual(expected, actual, places = 10, msg = None, delta = None)

if __name__ == '__main__':
    unittest.main(exit=False)