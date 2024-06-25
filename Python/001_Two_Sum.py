class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = {}
        n = len(nums)
        for i in range(n):
            hashtable[nums[i]] = i

        for i in range(n):
            comp = target - nums[i]
            if comp in hashtable and hashtable[comp] != i:
                return [i, hashtable[comp]]
