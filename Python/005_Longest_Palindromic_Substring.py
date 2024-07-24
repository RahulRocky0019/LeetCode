class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""
        elif len(s) == 1:
            return s

        result = ""
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                temp = s[i:j + 1]
                if temp == temp[::-1]:
                    result = temp if len(temp) > len(result) else result
        
        return result
