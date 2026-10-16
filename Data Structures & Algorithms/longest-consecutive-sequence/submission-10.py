class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        best = 0
        nums = set(nums)
        for num in nums: 
            if num - 1 not in nums: 
                len = 1
                while(num + len in nums): 
                    len += 1
                if len > best: 
                    best = len
        return best



