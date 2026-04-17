from bisect import bisect_left, bisect_right

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1
        return bisect_left(nums, target)