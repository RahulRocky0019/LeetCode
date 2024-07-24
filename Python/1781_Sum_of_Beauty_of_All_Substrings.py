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
                temp_l = Counter(temp).values()
                total += max(temp_l) - min(temp_l)
        
        return total
