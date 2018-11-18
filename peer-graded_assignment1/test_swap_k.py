import a1
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    # Add your test methods for a1.swap_k here.
    def test_swap_example_1(self):
        """Test L with even items and even swap#."""
		
        actual = a1.swap_k([1, 2, 3, 4, 5, 6], 2)
        expected = [5, 6, 3, 4, 1, 2]
        self.assertEqual(expected, actual)
    def test_swap_example_2(self):
        """Test L with odd items and odd swap#."""
		
        actual = a1.swap_k([1, 2, 3, 4, 5, 6, 7], 3)
        expected = [5, 6, 7, 4, 1, 2, 3]
        self.assertEqual(expected, actual)
        
    def test_swap_example_3(self):
        """Test L with the smallest non-zero and non-1 item # list"""
		
        actual = a1.swap_k(["a", "b"], 1)
        expected = ["b", "a"]
        
        self.assertEqual(expected, actual)
    def test_swap_example_4(self):
        """Test L with an empty list"""
		
        actual = a1.swap_k([], 0)
        expected = []
        self.assertEqual(expected, actual)
        
    def test_swap_example_5(self):
        """Test L with a list of 1 item"""
		
        actual = a1.swap_k([1], 1)
        expected = [1]
        self.assertEqual(expected, actual)
        
    def test_swap_example_6(self):
        """Test L with a zero swap number"""
		
        actual = a1.swap_k([1, 2, 3, 4, 5, 6, 7], 0)
        expected = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main(exit=False)