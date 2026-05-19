class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max_value = max(prices)
        # min_value = min(prices)

        # max_index = prices.index(max_value)
        # min_index = prices.index(min_value)

        # if min_index < max_index :
        #     return max_value - min_value
    
        if prices is None:
            return 0
        distances = []
        size = len(prices)

        if size == 1:
            return 0
        for i in range(size):
            for j in range(i+1,size):
                value = prices[i] - prices[j]
                if value > 0:
                    distances.append(0)
                else:
                    distances.append(-value)

        return max(distances)