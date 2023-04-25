from random import randint
import unittest
from merge import merge_sort
 
class TestSum(unittest.TestCase):
 
    def test_insertion_sort(self):
        input  = [3,6,4,2,8,1]
 
        merge_sort(input,0,5)
 
        res = [1,2,3,4,6,8]
 
        self.assertListEqual(input,res)
 
 
if __name__ == '__main__':
    unittest.main()