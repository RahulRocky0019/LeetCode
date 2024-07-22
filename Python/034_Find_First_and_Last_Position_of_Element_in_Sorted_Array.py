class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def cond_binary_search(nums: List[int], n: int, target: int, bias: bool) -> int:
            low, high = 0, n - 1
            result = -1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    result = mid
                    if bias:
                        high = mid - 1
                    else:
                        low = mid + 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            
            return result

        floor = cond_binary_search(nums, len(nums), target, True)
        ceil = cond_binary_search(nums, len(nums), target, False)
        
        return [floor, ceil]
