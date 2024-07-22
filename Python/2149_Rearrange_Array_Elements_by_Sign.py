class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        pos, neg = 0, 1

        for i in nums:
            if i >= 0:
                result[pos] = i
                pos += 2
            else:
                result[neg] = i
                neg += 2
        
        return result
