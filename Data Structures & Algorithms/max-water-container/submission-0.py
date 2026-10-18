class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        curr = 0
        best = 0
        while r > l: 
            curr = (r - l) *  min(heights[l], heights[r])
            if curr > best:
                best = curr 
            if heights[l] <= heights[r]: 
                l += 1
            else: 
                r -= 1
        return best
        
            