class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        if x > 0:
            result = int(str(x)[::-1])
        elif x < 0:
            result = int(str(x)[1:][::-1]) * -1

        limit = [-2**31, 2**31 - 1]
        if result < limit[0] or result > limit[1]:
            return 0
                    
        return result
