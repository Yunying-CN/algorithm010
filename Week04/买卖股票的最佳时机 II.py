class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dic = {}
        dic[0] = 0
        for i in range(1, len(prices)):
            dic[i] = dic[i - 1] + max(0, prices[i] - prices[i - 1])
        return dic[len(prices) - 1]
