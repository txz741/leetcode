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
                if not temp:
                    res[1] += 1
                else:
                    res[0] += len(temp)

        return res


SS = Solution()
res = SS.masterMind('RGRB', 'BBBY')
print(res)