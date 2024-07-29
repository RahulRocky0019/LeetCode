class Solution:
    def climbStairs(self, n: int) -> int:
        
        # Approach 1
        # dp = [1] * (n+1)
        # dp[1] = 1

        # for i in range(2, n+1):
        #     dp[i] = dp[i - 1] + dp[i - 2]
        
        # return dp[n]

        # Approach 2
        prev2 = 1
        prev1 = 1
        prev = 1
        for _ in range(2, n + 1):
            prev = prev1 + prev2
            prev2 = prev1
            prev1 = prev
        
        return prev
