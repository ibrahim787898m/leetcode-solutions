"""
LeetCode Problem: 125. Valid Palindrome

Algorithm: Filter and normalize the string, then use two-pointer technique to check for palindrome.

Time Complexity: O(n) to process the string and O(n) for the two-pointer check -> O(n)

Space Complexity: O(n) for the filtered string -> O(n)
"""

class Solution(object):
    def isPalindrome(self, s):
        s = ''.join(ch for ch in s if ch.isalnum())
        s = s.lower()

        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False

            left += 1
            right -= 1
            
        return True
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome("A man, a plan, a canal: Panama"))  # True
    print(sol.isPalindrome("race a car"))                      # False
    print(sol.isPalindrome(" "))                                # True

"""
Optimization: Use two pointers directly on the original string without creating a filtered copy. This reduces space complexity to O(1). -> O(n) time, O(1) space.

Final Version ->
class Solution:
    def isPalindrome(self, s):
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1
            
        return True

Time Complexity: O(n)

Space Complexity: O(1)
"""