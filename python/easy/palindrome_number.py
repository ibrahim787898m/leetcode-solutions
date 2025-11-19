"""
LeetCode Problem: 9. Palindrome Number

Algorithm: Convert to string, reverse, compare.

Time Complexity: Convert + reverse + compare = O(d) where d is number of digits. -> O(d)

Space Complexity: Two strings (original + reversed) -> O(d)
"""

class Solution(object):
    def isPalindrome(self, x):
        s = str(x)
        rev = s[::-1]
        # print(reversed)

        if s == rev:
            return True
        else:
            return False
        
if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome(121))  # True
    print(sol.isPalindrome(-121)) # False
    print(sol.isPalindrome(10))  # False

"""
Optimization: Use integer math, no string conversion. -> O(d) time, O(1) space.

Final Version ->
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        rev = 0
        while x > rev:
            rev = rev * 10 + x % 10
            x //= 10

        return x == rev or x == rev // 10

Time Complexity: O(d)

Space Complexity: O(1)
"""