class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k < 0:
            return []
        nums.sort()

        # força bruta
        result = {}
        for i in range(len(nums)):
            cont = 1
            if nums[i] not in result:
                for j in range(i + 1, len(nums)):
                    if nums[i] == nums[j]:
                        cont += 1
                result[nums[i]] = cont

        final_result = sorted(result, key=result.get, reverse=True)[:k]
        return final_result
