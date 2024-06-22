class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        starting = self.mod_binary_search(nums, target, True)
        ending = self.mod_binary_search(nums, target, False)

        return [starting, ending]

    def mod_binary_search(self, nums: List[int], target: int, bias: bool) -> int:
        l, h = 0, len(nums) - 1
        i = -1

        while l <= h:
            mid = (l + h) // 2
            
            if target < nums[mid]:
                h = mid - 1
            elif target > nums[mid]:
                l = mid + 1
            else:
                i = mid
                if bias:
                    h = mid - 1
                else:
                    l = mid + 1
        
        return i
