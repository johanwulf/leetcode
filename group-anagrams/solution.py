from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """ 
        map = defaultdict(list) 

        for str in strs:
            key = [0] * 26
            for chr in str:
                key[ord(chr) - ord('a')] += 1
            map[tuple(key)].append(str)

        return list(map.values())
