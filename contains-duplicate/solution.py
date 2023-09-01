import unittest

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        values = set()
        for num in nums:
            if num in values:
                return True
            values.add(num)
        return False

class ContainsDuplicateTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_contains_duplicate_with_duplicates(self):
        nums = [1, 2, 3, 4, 5, 2]
        result = self.solution.containsDuplicate(nums)
        self.assertTrue(result)

    def test_contains_duplicate_without_duplicates(self):
        nums = [1, 2, 3, 4, 5]
        result = self.solution.containsDuplicate(nums)
        self.assertFalse(result)

    def test_contains_duplicate_empty_list(self):
        nums = []
        result = self.solution.containsDuplicate(nums)
        self.assertFalse(result)

unittest.main()
