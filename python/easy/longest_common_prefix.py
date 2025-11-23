"""
LeetCode Problem: 14. Longest Common Prefix

Algorithm: Vertical scanning of characters in strings.

Time Complexity: O(mn) where m is the length of the shortest string and n is the number of strings -> O(mn)

Space Complexity: O(1) for prefix storage -> O(1)
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        prefix = ""

        for i in range(len(strs[0])):
            first = strs[0][i]

            for char in strs[1:]:
                if i >= len(char) or char[i] != first:
                    return prefix
                
            prefix += first

        return prefix
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.longestCommonPrefix(["flower","flow","flight"]))  # Output: "fl"
    print(sol.longestCommonPrefix(["dog","racecar","car"]))    # Output: ""


"""
Optimization: Vertical scanning with slicing to reduce comparisons.

Final Version ->
class Solution:
def longestCommonPrefix(self, strs: List[str]) -> str:
    if not strs:
        return ""

    min_len = min(len(s) for s in strs)

    for i in range(min_len):
        char = strs[0][i]
        for s in strs[1:]:
            if any(s[i] != char for s in strs[1:]):
                return strs[0][:i]
                
    return strs[0][:min_len]

Time Complexity: O(mn)

Space Complexity: O(1)
"""