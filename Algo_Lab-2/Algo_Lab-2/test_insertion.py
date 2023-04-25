from random import randint
import unittest
from insertion import insertion_sort

class TestSum(unittest.TestCase):
 
    def test_insertion_sort(self):
        input = [3,6,4,2,8,1]
        sorted = insertion_sort(input)
 
        res = [1,2,3,4,6,8]
 
        self.assertListEqual(res,sorted)
 
 
if __name__ == '__main__':
    unittest.main()