class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        currlen = 0
        bestlen = 0
        for i,num in enumerate(nums): 
            if i == 0:
                currlen = 1
            else: 
                if num == nums[i-1] + 1: 
                    currlen += 1
                else: 
                    bestlen = currlen if currlen > bestlen else bestlen
                    currlen = 1
        bestlen = currlen if currlen > bestlen else bestlen
        return bestlen