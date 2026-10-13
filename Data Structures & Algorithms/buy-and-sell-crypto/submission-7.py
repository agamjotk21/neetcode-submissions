class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        best = 0

        while sell < len(prices): 
            if prices[sell] > prices[buy]:
                if prices[sell] - prices[buy] > best: 
                    best = prices[sell] - prices[buy]
                sell += 1
            else: 
                buy = sell
                sell += 1
            
        return best


#buy 1
#sell 2
#prices[sell] 1
#prices[buy] 5
#best 4
