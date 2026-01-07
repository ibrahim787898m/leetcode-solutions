"""
LeetCode Problem: 3. Longest Substring Without Repeating Characters

Algorithm: Sliding Window + Hash Set.

Time Complexity: O(n) where n is the length of s -> O(n)

Space Complexity: O(min(m, n)) where m is the size of the charset and n is the length of s -> O(min(m, n))
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = 0
        right = 0
        max_length = 0
        seen = set()

        while right < len(s):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            max_length = max(max_length, right - left + 1)
            right += 1

        return max_length
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstring("abcabcbb"))  # Output: 3
    print(sol.lengthOfLongestSubstring("bbbbb"))     # Output: 1
    print(sol.lengthOfLongestSubstring("pwwkew"))    # Output: 3

"""
Optimization: None needed, already optimal. -> O(n) time, O(min(m, n)) space. Just added edge case for empty input and slightly changed variable names for clarity.

Final Version ->
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0

        left = 0
        right = 0
        max_length = 0
        seen = set()

        while right < len(s):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            current_length = right - left + 1
            max_length = max(max_length, current_length)
            right += 1

        return max_length

Time Complexity: O(n) where n is the length of s -> O(n)

Space Complexity: O(min(m, n)) where m is the size of the charset and n is the length of s -> O(min(m, n))
"""