class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        counter = 0
        minpricesofar = float('inf')
        maxprofit = 0
        while counter < len(prices):
            if prices[counter] < minpricesofar:
                minpricesofar = prices[counter]
            maxprofit = max(maxprofit, prices[counter] - minpricesofar)
            counter += 1
        return maxprofit