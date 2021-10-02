import collections
from typing import List


class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        diff = sum(aliceSizes) - (sum(aliceSizes) + sum(bobSizes)) / 2
        aliceSizes = set(aliceSizes)
        bobSizes = set(bobSizes)
        # res = []
        for a in aliceSizes:
            if a - diff in bobSizes:
                return [a, a - diff]



SS = Solution()
res = SS.fairCandySwap([1, 1], [2, 2])
print(res)