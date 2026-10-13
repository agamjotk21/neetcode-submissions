class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valToInd = dict()

        for i, n in enumerate(nums): 
            valToInd[n] = i
        
        for i, n in enumerate(nums): 
            if target-n in valToInd and valToInd[target-n] != i: 
                compInd = valToInd[target-n]
                return [i,compInd] if i<compInd else [compInd,i]

