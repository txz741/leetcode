import collections
from typing import List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        length = len(nums) - 1
        hashmap = collections.Counter(nums)
        deg = hashmap[max(hashmap, key=hashmap.get)]
        res = float('inf')
        for i, n in enumerate(nums):
            if n in hashmap and hashmap[n] == deg:
                j = length
                while nums[j] != n:
                    j -= 1
                if j >= i:
                    res = min(res, j - i + 1)
                hashmap.pop(n)

        return res


SS = Solution()
res = SS.findShortestSubArray([1,2,2,3,1,4,2])
print(res)