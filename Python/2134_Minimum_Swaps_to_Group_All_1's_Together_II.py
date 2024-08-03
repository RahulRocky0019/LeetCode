class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        total = sum(nums)
        n = len(nums)

        if total == 0 or total == n:
            return 0

        current_1 = sum(nums[:total])
        max_1 = current_1

        for i in range(n):
            current_1 += nums[(i + total) % n]
            current_1 -= nums[i]
            max_1 = max(max_1, current_1)

        return total - max_1
