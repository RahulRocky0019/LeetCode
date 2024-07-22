from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Approach 1
        # map = Counter(nums)
        # for i, j in map.items():
            # if j > len(nums) // 2:
                # return i
        # 
        # return -1

        # Approach 2
        count = 0
        result = 0

        for i in nums:
            if count == 0:
                result = i
            if i == result:
                count += 1
            else:
                count -= 1
        
        return result
