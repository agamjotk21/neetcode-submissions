class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums: 
            count[num] = 1 if num not in count else count[num] + 1
        
        pairs = sorted(count.items(), key = lambda x:x[1])
        result = []
        i = 0
        while i < k: 
            result.append(pairs.pop()[0])
            i+=1
        
        return result

