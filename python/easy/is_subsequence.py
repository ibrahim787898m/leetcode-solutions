"""
LeetCode Problem: 392. Is Subsequence

Algorithm: Two-pointer (Greedy) technique to check subsequence.

Time Complexity: O(n) where n is the length of string t -> O(n)

Space Complexity: O(1) for pointer storage -> O(1)
"""

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        i = 0

        for char in t:
            if i < len(s) and s[i] == char:
                i += 1

        return i == len(s)
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.isSubsequence("abc", "ahbgdc"))  # Output: True
    print(sol.isSubsequence("axc", "ahbgdc"))  # Output: False

"""
Optimization: Early termination if all characters of s are found in t. -> O(n) time, O(1) space.

Final Version ->
class Solution:
def isSubsequence(self, s: str, t: str) -> bool:
    if not s:
        return True

    i = 0
    for char in t:
        if s[i] == char:
            i += 1
            if i == len(s):
                return True

    return False

Time Complexity: O(n)

Space Complexity: O(1)
"""