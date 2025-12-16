"""
LeetCode Problem: 344. Reverse String

Algorithm: Two-pointer approach with a helper function to reverse the string in place.

Time Complexity: O(n) where n is the length of s -> O(n)

Space Complexity: O(1) for in-place reversal -> O(1)
"""

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        n = len(s)

        def reversed(s, l, r):
            while l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1

            return s

        reversed(s, 0, n - 1)

        return s

if __name__ == "__main__":
    sol = Solution()
    print(sol.reverseString(["h","e","l","l","o"]))  # ["o","l","l","e","h"]
    print(sol.reverseString(["H","a","n","n","a","h"])) # ["h","a","n","n","a","H"]

"""
Optimization: Direct two-pointer swap without helper function. -> O(n) time, O(1) space.

Final Version ->
class Solution:
    def reverseString(self, s: list[str]) -> None:
        left, right = 0, len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return s

Time Complexity: O(n)

Space Complexity: O(1)
"""
    