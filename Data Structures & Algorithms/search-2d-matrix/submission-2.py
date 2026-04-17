from bisect import bisect_left

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            value = bisect_left(matrix[i], target)
            if value < n and matrix[i][value] == target:
                return True
                
        return False
