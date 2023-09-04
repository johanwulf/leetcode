from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        values = {}
        freq = [[] for _ in range(len(nums) + 1)] 

        for num in nums:
            values[num] = 1 + values.get(num, 0)
        for n, c in values.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        return []
