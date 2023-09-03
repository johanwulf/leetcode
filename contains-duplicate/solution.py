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
