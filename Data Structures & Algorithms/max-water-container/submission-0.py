class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxArea = 0

        while l < r: 
            width = r - l 
            height = min(heights[l], heights[r]) #min()b/c the shorter wall limits how high the water can go.
            area = width * height
            maxArea = max(maxArea, area) 

            if (heights[l] < heights[r]):
                l += 1
            else:
                r -= 1 
        return maxArea


        
        