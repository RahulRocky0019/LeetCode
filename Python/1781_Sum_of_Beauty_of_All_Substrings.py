from collections import Counter

class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        total = 0
        if n == 1:
            return total

        for i in range(n):
            for j in range(i + 1, n + 1):
                temp = s[i:j]
                temp_l = list(Counter(temp).items())
                temp_l.sort(key = lambda x:x[1], reverse = True)
                total += temp_l[0][1] - temp_l[-1][1]
        
        return total
