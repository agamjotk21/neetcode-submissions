class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numZeros = nums.count(0)
        res = []
        product = 1
        if numZeros >= 2: 
            return [0 for i in range(len(nums))]
        elif numZeros == 1:
            for val in nums: 
                product *= val if val != 0 else 1
            for i in range(len(nums)): 
                if nums[i] != 0:
                    res.append(0)
                else: 
                    res.append(product)
            return res
        else:
            print("here")
            for val in nums: 
                product *= val
            for val in nums: 
                res.append(product//val)
            return res

