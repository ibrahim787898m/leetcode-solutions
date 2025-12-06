"""
LeetCode Problem: 121. Best Time to Buy and Sell Stock

Algorithm: Single pass greedy approach to track the minimum price and calculate the maximum profit.

Time Complexity: O(n) where n is the length of prices -> O(n)

Space Complexity: O(1) for storing min_price and max_profit -> O(1)
"""

class Solution(object):
    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit([7,1,5,3,6,4]))  # 5
    print(sol.maxProfit([7,6,4,3,1]))    # 0

"""
Optimization: More pythonic / Compact. -> O(n) time, O(1) space.

Final Version ->
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)

        return max_profit

Time Complexity: O(n) where n is the length of prices -> O(n)

Space Complexity: O(1) for storing min_price and max_profit -> O(1)
"""