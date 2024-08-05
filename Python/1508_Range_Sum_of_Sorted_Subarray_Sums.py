MOD = 10**9 + 7

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sub_array = []

        for i in range(len(nums)):
            temp = 0
            for j in range(i, len(nums)):
                temp += nums[j]
                sub_array.append(temp)
        
        sorted_array = sorted(sub_array)

        print(sorted_array)

        return sum(sorted_array[left-1:right]) % MOD
