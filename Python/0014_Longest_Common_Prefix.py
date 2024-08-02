class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = len(strs[0])
        for s in strs:
            min_len = min(min_len, len(s))
        
        result = ""
        for i in range(min_len):
            char = strs[0][i]
            for s in strs:
                if s[i] != char:
                    return result
            result += char
        
        return result
