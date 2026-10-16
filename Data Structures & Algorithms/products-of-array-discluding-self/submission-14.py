class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        totalProd = 1
        for num in nums:
            if num != 0: 
                totalProd *= num
        print(totalProd)
        res = []
        countZero = nums.count(0)
        for num in nums:
            if countZero == 1:
                res.append(0 if num != 0 else totalProd)
            elif countZero > 1: 
                res = [0] * len(nums)
            else: 
                res.append(int(totalProd / num if num != 0 else 0))
        return res