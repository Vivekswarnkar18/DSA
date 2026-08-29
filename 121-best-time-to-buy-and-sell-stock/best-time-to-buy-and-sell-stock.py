class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy=prices[0]
        profit=0
        n=len(prices)
        for i in range(0,n):
            if prices[i]<buy:
                buy=prices[i]
            else:
                profit=max(profit,prices[i]-buy)
        return profit