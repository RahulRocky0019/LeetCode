from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # Approach 1
        # return True if sorted(s) == sorted(t) else False

        # Approach 2
        hash_s = Counter(s)
        hash_t = Counter(t)
        
        if hash_s == hash_t:
            return True
        else:
            return False

