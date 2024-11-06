class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        least = prices[0]
        total = 0

        for i in range(len(prices)):
            if prices[i]<least:
                least = prices[i]
            if prices[i]-least > total:
                total = prices[i]-least

        return total