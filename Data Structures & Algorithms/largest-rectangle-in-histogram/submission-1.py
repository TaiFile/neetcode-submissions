class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        size = len(heights)
        max_area = 0
        for i in range(size):
            temp = heights[i]
            for j in range(i, size):
                temp = min(temp, heights[j])
                area = temp * (j - i + 1)
                max_area = max(max_area, area)
                
        return max_area