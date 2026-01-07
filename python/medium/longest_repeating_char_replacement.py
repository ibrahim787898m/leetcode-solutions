"""
LeetCode Problem: 424. Longest Repeating Character Replacement

Algorithm: Sliding Window + Character Frequency Count.

Time Complexity: O(n) where n is the length of s -> O(n)

Space Complexity: O(1) for the count dictionary (fixed size of alphabet) -> O(1)
"""

class Solution(object):
    def characterReplacement(self, s, k):
        left = 0
        right = 0
        max_count = 0
        count = {}

        while right < len(s):
            count[s[right]] = count.get(s[right], 0) + 1
            max_count = max(max_count, count[s[right]])

            if right - left + 1 - max_count > k:
                count[s[left]] -= 1
                left += 1

            right += 1

        return right - left
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.characterReplacement("ABAB", 2))  # Output: 4
    print(sol.characterReplacement("AABABBA", 1))  # Output: 4

"""
Optimization: None needed, already optimal. -> O(n) time, O(1) space. Just added edge case for empty input and slightly changed variable names for clarity.

Final Version ->
class Solution(object):
    def characterReplacement(self, s, k):
        if not s:
            return 0

        left = 0
        right = 0
        max_count = 0
        count = {}

        while right < len(s):
            count[s[right]] = count.get(s[right], 0) + 1
            max_count = max(max_count, count[s[right]])

            if right - left + 1 - max_count > k:
                count[s[left]] -= 1
                left += 1

            right += 1

        return right - left

Time Complexity: O(n) where n is the length of s -> O(n)

Space Complexity: O(1) for the count dictionary (fixed size of alphabet) -> O(1)
"""