class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = 0
        end = 1
        ans = 0
        while end < len(prices):
            if prices[start] >= prices[end]:
                start = end
                end += 1
            elif prices[end] > prices[start]:
                temp = prices[end]-prices[start]
                if temp > ans:
                    ans = temp
                end += 1
        return ans