class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set(['q','w','e','r','t','y','u','i','o','p'])
        row2 = set(['a','s','d','f','g','h','j','k','l'])
        row3 = set(['z','x','c','v','b','n','m'])

        result = []
        for word in words:
            temp = set(word.lower())
            print(temp)
            if len(row1.union(temp)) == len(row1):
                result.append(word)
            elif len(row2.union(temp)) == len(row2):
                result.append(word)
            elif len(row3.union(temp)) == len(row3):
                result.append(word)
        
        return result
