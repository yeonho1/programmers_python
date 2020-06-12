import unittest
from solution import solution

class SolutionTest(unittest.TestCase):
    test_cases = [
        ("leo", (["leo", "kiki", "eden"], ["eden", "kiki"])),
        ("vinko", (["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"])),
        ("mislav", (["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))
    ]
    def test_solution(self):
        for i, (expected, args) in enumerate(self.test_cases, start=1):
            print('Test Case %d' % i)
            result = solution(*args)
            self.assertEqual(result, expected)
            print('Completed')
if __name__ == '__main__':
    unittest.main()