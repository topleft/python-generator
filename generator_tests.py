import unittest
from generator import *

class SeqGenTest(unittest.TestCase):

    def test_first_N(self):
        self.assertEqual(first_N(0), 0.0) 
        self.assertEqual(first_N(1), 1.0) 
        self.assertEqual(first_N(2), 1.5) 
        self.assertEqual(first_N(3), 1.75) 
        self.assertEqual(first_N(4), 1.875) 

    def test_until_small(self):
        self.assertEqual(until_small(1.0 / 2), 1.5) 
        self.assertEqual(until_small(1.0 / 8), 1.875) 

if __name__ == '__main__':
    unittest.main()