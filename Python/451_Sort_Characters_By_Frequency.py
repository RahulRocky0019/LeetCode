from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        map = Counter(s)
        sorted_map = sorted(map.items(), key = lambda x: x[1], reverse = True)
        result = []
        for i, j in sorted_map:
            result.append(i*j)
        
        return "".join(result)
