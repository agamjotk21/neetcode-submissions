class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        letterFreq = dict()
        for word in strs: 
            sortedWord = ''.join(sorted(word))
            if letterFreq.get(sortedWord) == None:
                letterFreq[sortedWord] = [word]
            else: 
                letterFreq[sortedWord].append(word)
        result = []
        for key in letterFreq: 
            result.append(letterFreq[key])

        return result

        letterFreq = defaultdict(list)
        for word in strs: 
            sortedW = ''.join(sorted(word))
            letterFreq[sortedW].append(word)
        return [letterFreq.values()]
                    
            
