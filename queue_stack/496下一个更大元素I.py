import collections
from typing import List

# 用到单调栈，每次都是小的先出栈，从而保证了顺序的单调不降
# 出栈的同时记录下是什么元素让他出栈的，构建了哈希表，从而就能确定下一个更大的元素是什么，直接查表就有了

class Solution:
    def nextGreaterElement(self, nums1: List[int],
                           nums2: List[int]) -> List[int]:
        hashmap = dict()
        stack = collections.deque()
        for num in nums2:
            while len(stack) > 0 and stack[-1] < num:
                hashmap[stack.pop()] = num
            stack.append(num)

        res = []
        for num in nums1:
            if num in hashmap:
                res.append(hashmap[num])
            else:
                res.append(-1)
        return res

SS = Solution()
res = SS.nextGreaterElement([4, 1, 2], [1, 3, 4, 2])