"""
LeetCode Problem: 242. Valid Anagram

Algorithm: Sort both strings and compare.

Time Complexity: O(n log n) due to sorting both strings of length n.

Space Complexity: O(1) if sorting in place, otherwise O(n) for storing sorted strings.
"""

class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.isAnagram("anagram", "nagaram"))  # True
    print(sol.isAnagram("rat", "car"))          # False

"""
Optimization: Use a hash map to count character frequencies for O(n) time and O(1) space (since the character set is fixed). -> O(n) time, O(1) space

Final Version ->
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}

        for char in s:
            count[char] = count.get(char, 0) + 1

        for char in t:
            if char not in count:
                return False
            
            coutnt[char] -= 1

            if count[char] < 0:
                return False

            return True

Time Complexity: O(n)

Space Complexity: O(1)
"""