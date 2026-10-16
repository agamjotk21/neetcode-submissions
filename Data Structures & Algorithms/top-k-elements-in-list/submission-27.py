class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)
        for num in nums: 
            freqs[num] += 1
        
        listFreqs = []
        for elem in freqs: 
            listFreqs.append([freqs[elem], elem])
        listFreqs = sorted(listFreqs, reverse = True)
        res = []
        for i in range(k): 
            res.append(listFreqs[i][1])
        return res

