class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        nums = list(set(nums)) 
        nums.sort()
        cont = 1
        result = 1
        for i in range(len(nums) - 1):
            if nums[i+1] == nums[i] + 1:
                cont +=1
            else:
                result = max(result,cont)
                cont = 1

        result = max(result,cont)
        return result
