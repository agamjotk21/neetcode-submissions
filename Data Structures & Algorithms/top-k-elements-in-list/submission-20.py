class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        pairs = sorted(count.items(), key=lambda x: x[1])
        return [pair[0] for pair in pairs[-k:]]
