# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         nums.sort()
#         size = len(nums)
#         result = []
#         for i in range(size):
#             for j in range(i+1, size):
#                 target = (nums[i] + nums[j]) * -1
#                 if target in nums:
#                     k = nums.index(target)
#                     if k != i and k!= j:
#                         result.append([nums[i], nums[j], target])
#         return result
        
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # 1. Ordena o array
        result = []
        
        for i in range(len(nums) - 2):  # 2. Fixa o primeiro elemento
            
            # 3. Pula duplicatas do i
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left = i + 1
            right = len(nums) - 1
            
            while left < right:  # 4. Dois ponteiros
                soma = nums[i] + nums[left] + nums[right]
                
                if soma == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    # Pula duplicatas do left e right
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                    
                elif soma < 0:
                    left += 1   # precisa de valor maior
                else:
                    right -= 1  # precisa de valor menor
        
        return result