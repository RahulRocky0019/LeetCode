class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash_st = {}
        hash_ts = {}

        for i in range(len(s)):
            hash_st[s[i]] = t[i]
            hash_ts[t[i]] = s[i]
        
        for i in range(len(s)):
            if hash_st[s[i]] != t[i] or hash_ts[t[i]] != s[i]:
                return False
        
        return True
