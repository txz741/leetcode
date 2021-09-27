import collections
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        mylist = []
        i, length = 0, len(paragraph)
        while i < length:
            if paragraph[i].isalpha():
                if mylist:
                    mylist[-1] += paragraph[i].lower()
                else:
                    mylist.append(paragraph[i].lower())
            else:
                while i < length and not paragraph[i].isalpha():
                    i += 1
                if i < length:
                    mylist.append(paragraph[i].lower())
            i += 1
        return mylist


SS = Solution()
res = SS.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", 'a')
print(res)