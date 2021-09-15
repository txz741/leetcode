from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        res = [[1], [1, 1]]
        for i in range(2, numRows):
            for j in range(i + 1):
                if j == 0:
                    res.append([1])
                elif 0 < j < i:
                    res[i].append(res[i - 1][j - 1] + res[i - 1][j])
                else:
                    res[i].append(1)
        return res

SS = Solution()
res = SS.generate(5)
print(res)