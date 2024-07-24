class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        sign = 1
        result = []

        while i < n and s[i] == " ":
            i += 1

        if i < n and s[i] in "+-":
            sign = -1 if s[i] == "-" else 1
            i += 1
        
        while i < n and ord("0") <= ord(s[i]) <= ord("9"):
            result.append(s[i])
            i += 1
        
        if len(result) == 0:
            return 0
        
        num = int("".join(result)) * sign
        if num > 2**31 - 1:
            return 2**31 - 1
        elif num < -2**31:
            return -2**31
        else:
            return num
