import heapq

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = []
        heapq.heapify(heap)
        duplicate = set()
        
        heapq.heappush(heap, 1)
        for _ in range(n):
            a = heapq.heappop(heap)
            if a*2 not in duplicate:
                heapq.heappush(heap, a*2)
                duplicate.add(a*2)
            if a*3 not in duplicate:
                heapq.heappush(heap, a*3)
                duplicate.add(a*3)
            if a*5 not in duplicate:
                heapq.heappush(heap, a*5)
                duplicate.add(a*5)
        
        return a
