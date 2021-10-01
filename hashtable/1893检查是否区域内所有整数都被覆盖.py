#%%
# 很妙的位运算求解方法
from typing import List


class Solution:
    def isCovered(self, ranges: List[List[int]], left: int,
                  right: int) -> bool:
        data = 0
        for r in ranges:
            data |= (1 << (r[1] + 1)) - (1 << r[0])
        temp = (1 << (right + 1)) - (1 << left)
        return (temp & data) == temp

SS = Solution()
res = SS.isCovered([[1, 2], [3, 4], [5, 6]], 2, 5)
print(res)

#%%
# 很妙的差分数组解法。由于题目是说数组长度只有50，所以构建了52长度的差分数组diff
# diff每一位都表示区间覆盖量相对于前一位的增量（可能为负数）
# 构建好diff后，求前缀和即可得到当前位置（数）i被多少区间给覆盖了
# 如果求和数量<=0则说明该位置没有被区间覆盖
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        diff = [0] * 52   # 差分数组
        for l, r in ranges:
            diff[l] += 1
            diff[r+1] -= 1
        # 前缀和
        curr = 0
        for i in range(1, 51):
            curr += diff[i]
            if left <= i <= right and curr <= 0:
                return False
        return True


SS = Solution()
res = SS.isCovered([[1, 2], [3, 4], [5, 6]], 2, 5)
print(res)