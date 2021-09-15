class Solution:
    def modifyString(self, s: str) -> str:
        length = len(s)
        s = list(s)
        for i, n in enumerate(s):
            if n == '?':
                ahead = ' ' if i == 0 else s[i - 1]
                behind = ' ' if i == length - 1 else s[i + 1]
                temp = 'a'
                while (temp == ahead or temp == behind):
                    temp = chr((ord(temp) + 1))
                s[i] = temp
        return ''.join(s)

# class Solution:
#     def modifyString(self, s: str) -> str:
#         length = len(s)
#         s = list(s)
#         for i, n in enumerate(s):
#             if n == '?':
#                 ahead = ' ' if i == 0 else s[i - 1]
#                 behind = ' ' if i == length - 1 else s[i + 1]
#                 temp = 'a'
#                 while (temp == ahead or temp == behind):
#                     temp = chr((ord(temp) + 1))
#                 s[i] = temp
#         return ''.join(s)


SS = Solution()
s = SS.modifyString('?asxxxe')
print(s)