class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        letRep = defaultdict(list)
        for word in strs: 
            currWordRep = [0] * 26
            for char in word:
                currWordRep[ord(char)-ord('a')] += 1
            letRep[tuple(currWordRep)].append(word)
        
        return list(letRep.values())
