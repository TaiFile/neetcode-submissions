class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # força bruta
        size = len(nums)
        result = []
        index = 0
        for i in range(size):
            cont = 1
            for j in range(0, size):
                if j != i:
                    cont *= nums[j]
            result.append(cont)
        return result