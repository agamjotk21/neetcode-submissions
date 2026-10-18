class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, num1 in enumerate(nums): 
            right = len(nums) - 1
            left = i + 1
            while right > left: 
                if nums[right] + nums[left] == -num1: 
                    if sorted([num1, nums[right], nums[left]]) not in res:
                        res.append(sorted([num1, nums[right], nums[left]]))
                    left += 1
                elif nums[right] + nums[left] > -num1: 
                    right -= 1
                else: 
                    left += 1
        return res
                

        