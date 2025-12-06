class Solution:
    def main(self, prices: list) -> int:
        max_profit = 0
        current_profit = 0

        for i in range(1, len(prices)):
            change = prices[i] - prices[i - 1]
            current_profit = max(0, current_profit + change)
            max_profit = max(max_profit, current_profit)
            
        return max_profit
                
        
if __name__ == "__main__":
    sol = Solution()
    print(sol.main([7,1,5,3,6,4]))  # 5
    print(sol.main([7,6,4,3,1]))    # 0
    print(sol.main([2,4,1]))        # 2
    print(sol.main([3,2,6,5,0,3]))  # 4
    print(sol.main([1,2]))          # 1
    print(sol.main([2,1]))          # 0
