import a1
import unittest


class TestNumBuses(unittest.TestCase):
    """ Test class for function a1.num_buses. """

    # Add your test methods for a1.num_buses here.
    def test_buses_example_1(self):
        """Test num_buses with 75."""
		
        actual = a1.num_buses(75)
        expected = 2
        self.assertEqual(expected, actual)
    def test_buses_example_2(self):
        """Test num_buses with 20."""
		
        actual = a1.num_buses(20)
        expected = 1
        self.assertEqual(expected, actual)
        
    def test_buses_example_3(self):
        """Test num_buses with 50."""
		
        actual = a1.num_buses(50)
        expected = 1
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main(exit=False)