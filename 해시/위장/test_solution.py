import unittest
from solution import solution

class SolutionTest(unittest.TestCase):
    test_cases = [
        (5, ([
            ["yellow_hat", "headgear"],
            ["blue_sunglasses", "eyewear"],
            ["green_turban", "headgear"],
        ],)),
        (3, ([
            ["crow_mask", "face"],
            ["blue_sunglasses", "face"],
            ["smoky_makeup", "face"],
        ],))
    ]
    def test_solution(self):
        for i, (expected, args) in enumerate(self.test_cases, start=1):
            print('Test Case %d' % i)
            result = solution(*args)
            self.assertEqual(result, expected)
            print('Completed')
if __name__ == '__main__':
    unittest.main()