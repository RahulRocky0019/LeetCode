from collections import defaultdict, Counter
import heapq

class Solution:
    def minimumPushes(self, word: str) -> int:
        # Approach 1
        # 
        # unique = Counter(word)
        # unique = dict(sorted(unique.items(), key=lambda x: x[1], reverse = True))
        # keys = 8
        # press = 1
        # i = 0
        # map = defaultdict(int)

        # for c in unique.keys():
        #     i += 1
        #     if i > keys:
        #         press += 1
        #         i = 1
        #     map[c] = press
        
        # print(map)
        # min_press = 0
        # for c in word:
        #     min_press += map[c]
        
        # return min_press

        
        # Approach 2
        freq = Counter(word)
        freq_list = []
        heapq.heapify(freq_list)
        
        for u, v in freq.items():
            heapq.heappush(freq_list, -v)
        
        min_press = 0
        idx = 0
        while freq_list:
            min_press += (idx // 8 + 1) * (heapq.heappop(freq_list) * (-1))
            idx += 1

        return min_press


