class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        new1 = []
        new2 = []
        n = len(nums)
        for i in nums:
            if i != 0:
                new1.append(i)
            else:
                new2.append(i)
        nums.extend(new1)
        nums.extend(new2)
        nums[:n] = []

        
