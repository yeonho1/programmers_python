import unittest
from solution import solution

class SolutionTest(unittest.TestCase):
    test_cases = [
        (8, (2, 10, [7, 4, 5, 6])),
        (101, (100, 100, [10])),
        (110, (100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
    ]
    def test_solution(self):
        for i, (expected, args) in enumerate(self.test_cases, start=1):
            print('Test Case %d' % i)
            result = solution(*args)
            self.assertEqual(result, expected)
            print('Completed')
if __name__ == '__main__':
    unittest.main()