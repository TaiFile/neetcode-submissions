class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)
        result = 0
        left = 0
        right = 1
        while right < size:
            if prices[left] > prices[right]:
                left = right  # ✅ achou preço menor, move left
            else:
                value = prices[right] - prices[left]
                result = max(result, value)  # ✅ guarda o maior lucro
            right += 1
        return result