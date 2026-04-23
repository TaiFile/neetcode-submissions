class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        size = len(nums)
        result = set()
        
        for i in range(size):
            for j in range(i + 1, size):
                target = (nums[i] + nums[j]) * -1
                # target precisa ser >= nums[j] pois array está ordenado
                # e estar na parte direita de j
                if target >= nums[j] and target in nums[j+1:]:
                    result.add((nums[i], nums[j], target))
        
        return [list(t) for t in result]