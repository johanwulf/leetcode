import unittest

class Solution(object):
    def isAnagramFirst(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t) 

    def isAnagramSecond(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        return countS == countT

class ContainsDuplicateTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_is_anagram_with_anagram(self):
        s = 'anagram'
        t = 'nagaram'
        result = self.solution.isAnagramFirst(s, t) & self.solution.isAnagramSecond(s, t)
        self.assertTrue(result)

    def test_is_anagram_without_anagram(self):
        s = 'rat'
        t = 'car'
        result = self.solution.isAnagramFirst(s, t) & self.solution.isAnagramSecond(s, t)
        self.assertFalse(result)

    def test_is_anagram_empty_strings(self):
        s = ''
        t = ''
        result = self.solution.isAnagramFirst(s, t) & self.solution.isAnagramSecond(s, t)
        self.assertTrue(result)

unittest.main()
