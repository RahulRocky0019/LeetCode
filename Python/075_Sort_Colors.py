class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Approach 1
        # nums.sort()
        
        # Approach 2
        map = {}
        for i in nums:
            map[i] = map.get(i, 0) + 1
        
        for i in range(map.get(0, 0)):
            nums[i] = 0
        for j in range(map.get(0, 0), map.get(0, 0) + map.get(1, 0)):
            nums[j] = 1
        for k in range(map.get(0, 0) + map.get(1, 0), len(nums)):
            nums[k] = 2
