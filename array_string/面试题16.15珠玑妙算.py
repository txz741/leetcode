from typing import List
class Solution:
    def masterMind(self, solution: str, guess: str) -> List[int]:
        res = [0, 0]
        hashmap1, hashmap2 = dict(), dict()
        for i, n in enumerate(zip(solution, guess)):
            if n[0] not in hashmap1:
                hashmap1[n[0]] = [i]
            elif n[0] in hashmap1:
                hashmap1[n[0]].append(i)
            if n[1] not in hashmap2:
                hashmap2[n[1]] = [i]
            elif n[1] in hashmap2:
                hashmap2[n[1]].append(i)

        for n in hashmap1:
            if n in hashmap2:
                temp = set(hashmap1[n]).intersection(set(hashmap2[n]))
                res[0] += len(temp) # 交集长度即为猜中个数
                res[1] += min(len(hashmap1[n]), len(hashmap2[n])) - len(temp) # 两个列表取最短且减去猜中个数即为伪猜中个数

        return res