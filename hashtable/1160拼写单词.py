import collections
from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        hashmap1 = collections.Counter(chars)
        res = 0

        for word in words:
            hashmap2 = collections.Counter(word)
            for ch in hashmap2:
                if hashmap1[ch] < hashmap2[ch]:
                    break
            else:
                res += len(word)

        return res
