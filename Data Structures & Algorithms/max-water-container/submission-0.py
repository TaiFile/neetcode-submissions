class Solution:
    def maxArea(self, heights: List[int]) -> int:
        size = len(heights)
        result = []
        for i in range(size):
            width = 1
            for j in range(i + 1, size):
                tmp = min(heights[i], heights[j]) * width
                width += 1
                result.append(tmp)
        return max(result)