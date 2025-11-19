"""
LeetCode Problem: 7. Reverse Integer

Algorithm: Convert integer to string, reverse it, handle sign and overflow.

Time Complexity: O(log n) where n is the absolute value of x -> O(log n)

Space Complexity: O(log n) for the string representation -> O(log n)
"""

class Solution:
    def reverse(self, x):
        if x < 0:
            s = (str(x)[1:])
            rev = s[::-1]
            res = int(rev) * -1
        else:
            res = int(str(x)[::-1])

        if res < -2**31 or res > 2**31 - 1:
            return 0
        
        return res
        
if __name__ == "__main__":
    sol = Solution()
    print(sol.reverse(123))   # Output: 321
    print(sol.reverse(-123))  # Output: -321
    print(sol.reverse(120))   # Output: 21

"""
Optimization: Use mathematical operations to reverse the integer without converting to string. This reduces space complexity to O(1). -> O(log n) time, O(1) space.

Final Version ->
class Solution:
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        x = abs(x)
        res = 0

        while x:
            res = res * 10 + x % 10
            x //= 10

        res *= sign

        if res < -2**31 or res > 2**31 - 1:
            return 0

        return res

Time Complexity: O(log n)

Space Complexity: O(1)
"""
