class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        size = len(temperatures)
        
        for i in range(size):
            cont = 0
            for j in range(i + 1, size):
                if temperatures[i] < temperatures[j]:
                    cont = j - i
                    break
            result.append(cont)
        return result