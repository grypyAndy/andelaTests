import unittest
from arithm import solution

class TestSolution(unittest.TestCase):
    def test_addition(self):
        self.assertTrue(solution(10,20,"+"),30)