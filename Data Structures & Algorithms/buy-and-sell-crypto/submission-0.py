class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # what is lowest value seen so far
        # what is profit if i sell today
        lowestSeen = 0
        maxProfit = 0

        for i in range(1,len(prices)):
            if prices[i-1] < prices[lowestSeen]:
                lowestSeen = i-1

            diff = prices[i] - prices[lowestSeen]
            if diff > maxProfit:
                maxProfit = diff

        return maxProfit
