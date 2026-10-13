class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numInd = dict()
        for i, num in enumerate(nums):
            numInd[num] = i
        
        for i, num in enumerate(nums): 
            diff = target - num
            if diff in numInd and numInd[diff] != i: 
                return [i, numInd[diff]]
            
