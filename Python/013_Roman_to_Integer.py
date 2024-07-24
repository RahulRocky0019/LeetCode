class Solution:
    def romanToInt(self, s: str) -> int:
        mem = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        result = 0
        n = len(s)
        for i in range(n):
            if i + 1 < n and mem[s[i]] < mem[s[i+1]]:
                result -= mem[s[i]]
            else:
                result += mem[s[i]]
        
        return result
