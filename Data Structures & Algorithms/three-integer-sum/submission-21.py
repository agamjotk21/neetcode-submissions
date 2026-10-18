class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, num1 in enumerate(nums): 
            if i > 0 and num1 == nums[i-1]: 
                continue
            right = len(nums) - 1
            left = i + 1
            while right > left: 
                if nums[right] + nums[left] == -num1: 
                    res.append(sorted([num1, nums[right], nums[left]]))
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif nums[right] + nums[left] > -num1: 
                    right -= 1
                else: 
                    left += 1
        return res
                

        