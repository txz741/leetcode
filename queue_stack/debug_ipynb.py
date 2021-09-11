from typing import List
import collections


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        q = collections.deque()
        res = prices.copy()
        for i, p in enumerate(prices):
            while len(q) > 0 and prices[q[-1]] >= p:
                res[q[-1]] = prices[q[-1]] - p
                q.pop()
            q.append(i)
        return res


SS = Solution()
res = SS.finalPrices([8, 7, 4, 2, 8, 1])
print(res)