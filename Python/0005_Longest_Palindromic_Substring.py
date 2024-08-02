# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         if len(s) == 0:
#             return ""
#         elif len(s) == 1:
#             return s

#         result = ""
#         for i in range(len(s)):
#             for j in range(i + 1, len(s) + 1):
#                 temp = s[i:j + 1]
#                 if temp == temp[::-1]:
#                     result = temp if len(temp) > len(result) else result
        
#         return result

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        reslen = 0
        n = len(s)

        for i in range(n):
            # Odd Palindrom
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                if len(s[l:r+1]) > reslen:
                    result = s[l:r+1]
                    reslen = r - l + 1
                l -= 1
                r += 1
            
            # Even Palindrom
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                if len(s[l:r+1]) > reslen:
                    result = s[l:r+1]
                    reslen = r - l + 1
                l -= 1
                r += 1

        return result
