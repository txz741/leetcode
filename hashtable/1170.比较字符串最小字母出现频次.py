import collections
from typing import List


class Solution:
    def numSmallerByFrequency(self, queries: List[str],
                              words: List[str]) -> List[int]:
        res = []
        for i, word in enumerate(words):
            word_map = collections.Counter(word)
            words[i] = word_map[min(word_map.keys())]

        for q in queries:
            q_map = collections.Counter(q)
            q_n = q_map[min(q_map.keys())]
            res.append(sum(i > q_n for i in words))
        return res

SS = Solution()
res = SS.numSmallerByFrequency(queries=["bba","abaaaaaa","aaaaaa","bbabbabaab","aba","aa","baab","bbbbbb","aab","bbabbaabb"], 
words=["aaabbb","aab","babbab","babbbb","b","bbbbbbbbab","a","bbbbbbbbbb","baaabbaab","aa"])
print(res)