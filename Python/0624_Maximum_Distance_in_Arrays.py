class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        largest = sorted(arrays, key=lambda x: x[-1], reverse=True)
        max1, max1_a = largest[0][-1], largest[0]
        max2, max2_a = largest[1][-1], largest[1]
        
        smallest = sorted(arrays, key=lambda x: x[0])
        min1, min1_a = smallest[0][0], smallest[0]
        min2, min2_a = smallest[1][0], smallest[1]

        if max1_a == min1_a:
            maxi = max(max1-min2, max2-min1)
        else:
            maxi = max1 - min1

        return abs(maxi)
