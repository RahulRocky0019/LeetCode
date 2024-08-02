class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1
        
        total = len(nums)
        a = nums[0]
        change = 1
        for i in range(1, len(nums)):
            if nums[i] == a:
                total -= 1
            else:
                a = nums[i]
                nums[change] = nums[i]
                change += 1
        
        return total
