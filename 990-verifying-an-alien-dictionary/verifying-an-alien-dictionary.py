class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {}
        for i in range(len(order)) :
            d[order[i]] = i
        for i in range(1,len(words)):
            j = 0
            while j < len(words[i]) and j<len(words[i-1]):
                if words[i][j]!=words[i-1][j]:
                    break
                j+=1
            if j==len(words[i]) and words[i]!=words[i-1]:
                return False
            if j<len(words[i]) and j<len(words[i-1]) and d[words[i][j]]<d[words[i-1][j]]:
                return False
        return True

            
        