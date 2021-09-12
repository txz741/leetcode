from typing import List
import collections


class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        q = []
        hashmap = dict()
        length = len(nums)
        for i, num in enumerate(nums):
            while q and nums[q[-1]] <= num:
                j = q.pop()
                hashmap[j] = i
            q.append(i)
        for i in q:
            hashmap[i] = -1

        res = 0
        for k in hashmap:
            flag = k
            while hashmap[k] in hashmap and k != hashmap[k]:
                k = hashmap[k]
            else:
                if k - flag > res:
                    res = k - flag

        return res


SS = Solution()
res = SS.maxWidthRamp([9, 8, 1, 0, 1, 9, 4, 0, 4, 1])
print(res)