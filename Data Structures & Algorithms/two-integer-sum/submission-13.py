class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:\
        # Força bruta
        # for i in range (len(nums)):
        #     for j in range (i + 1,len(nums)):
        #         if(nums[i] + nums[j] == target):
        #             print(i,j)
        #             return [i, j]

        # HashSet
        vistos = {}  # valor -> índice
        for i, num in enumerate(nums):
            complemento = target - num
            if complemento in vistos:
                return [vistos[complemento], i]
            vistos[num] = i

        return []  

           

