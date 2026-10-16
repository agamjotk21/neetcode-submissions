class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # nums = sorted(list(set(nums)))
        # currlen = 0
        # bestlen = 0
        # for i,num in enumerate(nums): 
        #     if i == 0:
        #         currlen = 1
        #     else: 
        #         if num == nums[i-1] + 1: 
        #             currlen += 1
        #         else: 
        #             bestlen = currlen if currlen > bestlen else bestlen
        #             currlen = 1
        # bestlen = currlen if currlen > bestlen else bestlen
        # return bestlen

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



