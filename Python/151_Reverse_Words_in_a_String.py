class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        result = words[::-1]

        return " ".join(result)
