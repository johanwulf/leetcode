import unittest

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {} 
        for idx, num in enumerate(nums):
            diff = target - num

            if diff in map:
                return [map[diff], idx]
            map[num] = idx 

class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_two_sum_one(self):
        input = [2, 7, 11, 15]
        target = 9
        expected = [0, 1]
        result = self.solution.twoSum(input, target)
        print(result)
        self.assertEqual(result, expected)

    def test_two_sum_two(self):
        input = [3, 2, 4]
        target = 6
        expected = [1, 2]
        result = self.solution.twoSum(input, target)
        self.assertEqual(result, expected)

    def test_two_sum_three(self):
        input = [3, 3]
        target = 6
        expected = [0, 1]
        result = self.solution.twoSum(input, target)
        self.assertEqual(result, expected)

unittest.main()
