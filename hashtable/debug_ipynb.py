import collections
from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        left, hashmap = set(), dict()
        # res = -1
        for pair in trust:
            left.add(pair[0])
            if pair[1] not in hashmap:
                hashmap[pair[1]] = 1
            else:
                hashmap[pair[1]] += 1

        for x in hashmap:
            if hashmap[x] == n - 1 and x not in left:
                return x
        return -1


SS = Solution()
res = SS.findJudge(1,[])
print(res)