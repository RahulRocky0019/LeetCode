class Solution:
    def maxDepth(self, s: str) -> int:
        opened = 0
        max_depth = 0
        for c in s:
            if c == "(":
                opened += 1
            if c == ")":
                opened -= 1
            max_depth = max(max_depth, opened)
        
        return max_depth
        
