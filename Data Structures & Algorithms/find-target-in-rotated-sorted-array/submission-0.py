class Solution:
    def search(self, nums: List[int], target: int) -> int:
        size = len(nums)
        if target not in nums:
            return -1
        pos = nums.index(target) 
        return size - (size - pos)