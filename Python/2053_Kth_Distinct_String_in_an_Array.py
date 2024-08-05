from collections import Counter
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        result = ""
        map = Counter(arr)
        incr = 0
        for c in arr:
            if map[c] == 1 and incr != k:
                incr += 1
            if map[c] == 1 and incr == k:
                result = c
                return result
        
        return result
