"""
LeetCode Problem: 383. Ransom Note

Algorithm: Hash map to count character frequencies.

Time Complexity: O(m + n) where m and n are lengths of ransomNote and magazine -> O(m+n)

Space Complexity: O(k) where k is the number of unique characters in magazine -> O(k)
"""

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        count = {}
        bool = True

        for char in magazine:
            count[char] = count.get(char, 0) + 1

        for char in ransomNote:
            if char not in count:
                bool = False
                break

            count[char] -= 1

            if count.get(char) < 0: #type: ignore
                bool = False
                break

        return bool
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.canConstruct("a", "b"))  # False
    print(sol.canConstruct("aa", "ab"))  # False
    print(sol.canConstruct("aa", "aab"))  # True

"""
Optimization: Counter with subtraction and all() check -> O(m + n) time, O(k) space.

Final Version ->
from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_count = Counter(ransomNote)
        magazine_count = Counter(magazine)

        return not (ransom_count - magazine_count)

Time Complexity: O(m + n) where m and n are lengths of ransomNote and magazine -> O(m+n)

Space Complexity: O(k) where k is the number of unique characters in magazine -> O(k)
"""