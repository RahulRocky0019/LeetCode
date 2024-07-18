class Solution:
    def check(self, nums: List[int]) -> bool:
        error = 0

        for i in range(len(nums)):
            if nums[i] > nums[(i + 1) % len(nums)]:
                error += 1
        
        return True if error <= 1 else False
