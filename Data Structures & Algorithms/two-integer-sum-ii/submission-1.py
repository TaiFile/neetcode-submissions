class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        size = len(numbers)
        for i in range(size):
            for j in range(i + 1, size):
                tmp = numbers[i] + numbers[j]
                if tmp == target:
                    return [i + 1, j + 1]
        return []