from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_hashmap = defaultdict(list)
        for word in strs:
            sorted_word = "".join(sorted(word))
            result_hashmap[sorted_word].append(word)
        return list(result_hashmap.values())
