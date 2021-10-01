import collections
from typing import List


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y = 0, 0
        hashmap = set()
        hashmap.add('0_0')
        for p in path:
            if p == 'N':
                y += 1
            elif p == 'S':
                y -= 1
            elif p == 'W':
                x -= 1
            elif p == 'E':
                x += 1
            temp = str(x) + '_' + str(y)
            if temp in hashmap:
                return True
            hashmap.add(temp)
        return False


SS = Solution()
res = SS.isPathCrossing('NESWW')
print(res)