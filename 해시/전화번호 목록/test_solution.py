import unittest
from solution import solution

class SolutionTest(unittest.TestCase):
    test_cases = [
        (False, (["119", "97674223", "1195524421"],)),
        (True, (["123", "456", "789"],)),
        (False, (["12", "123", "1235", "567", "88"],))
    ]
    def test_solution(self):
        for i, (expected, args) in enumerate(self.test_cases, start=1):
            print('Test Case %d' % i)
            result = solution(*args)
            self.assertEqual(result, expected)
            print('Completed')
if __name__ == '__main__':
    unittest.main()