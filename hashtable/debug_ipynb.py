import collections
from typing import List
class Solution:
    def shortestCompletingWord(self, licensePlate: str,
                               words: List[str]) -> str:
        hashmap1 = dict()
        for x in licensePlate:
            if x.isalpha():
                x = x.lower()
                if x in hashmap1:
                    hashmap1[x] += 1
                else:
                    hashmap1[x] = 1

        res = max(words, key=len) + 'a'

        for word in words:
            flag = 0
            hashmap2 = collections.Counter(word)
            for x in hashmap1:
                if x not in hashmap2 or hashmap2[x] < hashmap1[x]:
                    flag = 1
                    break
            if flag == 0 and len(word) < len(res):
                res = word

        return res


SS = Solution()
a, b = "iLMOl80", ["send", "why", "want", "program", "million", "wonder", "manager", "success", "likely", "them"]
res = SS.shortestCompletingWord(a, b)
print(res)
