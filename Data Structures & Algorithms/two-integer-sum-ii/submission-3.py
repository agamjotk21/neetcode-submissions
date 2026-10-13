class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        small, big = 0, len(numbers) - 1
        #remember to retunr thisi  one indexed 
        while big > small: 
            s = numbers[small] + numbers[big]
            if s == target: 
                return [small + 1, big + 1]
            elif s > target: 
                big -= 1
            else: 
                small += 1
        
