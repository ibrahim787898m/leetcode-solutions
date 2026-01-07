"""
LeetCode Problem: 76. Minimum Window Substring

Algorithm: Sliding Window + Two Hash Maps.

Time Complexity: O(|s| + |t|) where |s| and |t| are the lengths of strings s and t respectively -> O(|s| + |t|)

Space Complexity: O(|s| + |t|) for the two hash maps -> O(|s| + |t|)
"""

class Solution:
    def minWindow(self, s, t):
        if len(s) < len(t):
            return ""
        
        need = {}

        for i in range(len(t)):
            need[t[i]] = need.get(t[i], 0) + 1

        right = 0
        left = 0

        window = {}

        formed = 0
        required = len(need)

        min_window = (0, float("inf"))

        while right < len(s):
            window[s[right]] = window.get(s[right], 0) + 1

            if s[right] in need and window[s[right]] == need[s[right]]:
                formed += 1

            while formed == required:
                if right - left + 1 < min_window[1]:
                    min_window = (left, right - left + 1)

                window[s[left]] -= 1

                if s[left] in need and window[s[left]] < need[s[left]]:
                    formed -= 1

                left += 1

            right += 1

        return "" if min_window[1] == float("inf") else s[min_window[0]: min_window[0] + min_window[1]]
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.minWindow("ADOBECODEBANC", "ABC"))  # Output: "BANC"
    print(sol.minWindow("a", "a"))  # Output: "a"
    print(sol.minWindow("a", "aa"))  # Output: ""

"""
Optimization: None needed, already optimal. -> O(|s| + |t|) time, O(|s| + |t|) space. Just added edge case for when s is shorter than t.

Final Version ->
class Solution:
    def minWindow(self, s, t):
        if len(s) < len(t):
            return ""
        
        need = {}

        for i in range(len(t)):
            need[t[i]] = need.get(t[i], 0) + 1

        right = 0
        left = 0

        window = {}

        formed = 0
        required = len(need)

        min_window = (0, float("inf"))

        while right < len(s):
            window[s[right]] = window.get(s[right], 0) + 1

            if s[right] in need and window[s[right]] == need[s[right]]:
                formed += 1

            while formed == required:
                if right - left + 1 < min_window[1]:
                    min_window = (left, right - left + 1)

                window[s[left]] -= 1

                if s[left] in need and window[s[left]] < need[s[left]]:
                    formed -= 1

                left += 1

            right += 1

        return "" if min_window[1] == float("inf") else s[min_window[0]: min_window[0] + min_window[1]]

Time Complexity: O(|s| + |t|) where |s| and |t| are the lengths of strings s and t respectively -> O(|s| + |t|)

Space Complexity: O(|s| + |t|) for the two hash maps -> O(|s| + |t|)
"""