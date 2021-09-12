from typing import List
import collections


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []
        index = 0
        flag = 0
        length = len(asteroids)
        while index < length and asteroids[index] < 0:
            s.append(asteroids[index])
            index += 1
        if index == length:
            return asteroids

        for i in range(index, length):
            if asteroids[i] > 0:
                s.append(asteroids[i])
            else:
                while len(s) > 0 and s[-1] > 0 and s[-1] <= abs(asteroids[i]):  # 栈顶是正的就开创
                    # x = s.pop()
                    if s.pop() == abs(asteroids[i]):  # 同归
                        flag = 1
                        break
                if (len(s) == 0 or s[-1] < 0) and flag !=1:  # 判定跳出while的条件 全创完了或栈顶是负的
                    s.append(asteroids[i])
                else:  # 新来的没创得过
                    pass
                flag = 0
        return s


SS = Solution()
res = SS.asteroidCollision([5, 10, -5])
print(res)