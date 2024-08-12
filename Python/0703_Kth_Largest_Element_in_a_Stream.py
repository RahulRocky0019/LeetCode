import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.lst = []

        for i in nums:
            self.add(i)

    def add(self, val: int) -> int:
        if (len(self.lst)) < self.k or self.lst[0] < val:
            heapq.heappush(self.lst, val)
        if len(self.lst) > self.k:
            heapq.heappop(self.lst)
        
        return self.lst[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
