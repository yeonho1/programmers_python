import unittest
from solution import solution

class SolutionTest(unittest.TestCase):
    test_cases = [
        ([4, 1, 3, 0], ([
            "classic", "pop", "classic", "classic", "pop"
        ],[
            500, 600, 150, 800, 2500
        ]))
    ]
    def test_solution(self):
        for i, (expected, args) in enumerate(self.test_cases, start=1):
            print('Test Case %d' % i)
            result = solution(*args)
            self.assertEqual(result, expected)
            print('Completed')
if __name__ == '__main__':
    unittest.main()