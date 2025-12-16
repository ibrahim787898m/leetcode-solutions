"""
LeetCode Problem: 509. Fibonacci Number

Algorithm: Recursive approach.

Time Complexity: O(2^n) due to the binary tree of calls. -> O(2^n)

Space Complexity: O(n) for the call stack. -> O(n)
"""

class Solution(object):
    def fib(self, n):
        if n <= 1:
            return n
        
        return self.fib(n -1) + self.fib(n - 2)
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.fib(2))  # Output: 1
    print(sol.fib(3))  # Output: 2
    print(sol.fib(4))  # Output: 3

"""
Optimization: Iterative approach for O(n) time and O(1) space. -> O(n) time, O(1) space.

Final Version ->
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        prev, curr = 0, 1

        for _ in range(2, n + 1):
            prev, curr = curr, prev + curr

        return curr

Time Complexity: O(n) where n is the input number -> O(n)

Space Complexity: O(1) for storing prev and curr -> O(1)
"""