class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=0
        profit=0
        for i in range(len(prices)-1):
            if prices[i+1]>prices[i]:
                profit=prices[i+1]-prices[i]
                res+=profit
        return res



        