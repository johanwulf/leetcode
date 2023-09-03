from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
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
