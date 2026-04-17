class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k < 0:
            return []
        nums.sort()

        # força bruta
        # result = {}
        # for i in range(len(nums)):
        #     cont = 1
        #     if nums[i] not in result:
        #         for j in range(i + 1, len(nums)):
        #             if nums[i] == nums[j]:
        #                 cont += 1
        #         result[nums[i]] = cont

        # final_result = sorted(result, key=result.get, reverse=True)[:k]
        # return final_result

        # Versão otimizada
        # hash = defaultdict(int)
        # for num in nums:
        #     key = num
        #     cont = 1
        #     if key not in hash:
        #         hash[key] = 1
        #     else:
        #         hash[key] += 1

        # chaves_ordenadas = sorted(hash, key=hash.get, reverse=True)
        # top_k = chaves_ordenadas[:k]
        # return top_k

        answer = []
        hold = {}

        for i in range(len(nums)):
            if hold.get(nums[i]) == None:
                hold[nums[i]] = 1 
            else:
                hold[nums[i]]+=1
        
        new_hold = sorted(hold, key=hold.get, reverse=True )
        for i in range(k):
            answer.append(new_hold[i])
        return answer