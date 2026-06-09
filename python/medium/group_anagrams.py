"""
LeetCode Problem: 49. Group Anagrams

Algorithm: Count character frequency as key in a hash map.

Time Complexity: O(n * k) where n is number of strings and k is max length of a string -> O(nk)

Space Complexity: O(n * k) for storing all anagrams -> O(nk)
"""

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict
        
        anagrams = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            key = tuple(count)
            anagrams[key].append(word)

        return list(anagrams.values())
        
if __name__ == "__main__":
    sol = Solution()
    print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(sol.groupAnagrams([""]))  # [[""]]
    print(sol.groupAnagrams(["a"])) # [["a"]]

"""
Optimization: Using sorted string as key instead of character count. Slightly slower for long strings. Use it when k is small. -> O(n k log k) time, O(nk) space.

Final Version ->
class Solution:
    def groupAnagrams(self, strs):
        from collections import defaultdict
        
        anagrams = defaultdict(list)

        for word in strs:
            key = ''.join(sorted(word))
            anagrams[key].append(word)

        return list(anagrams.values())

Time Complexity: O(n k log k)

Space Complexity: O(n * k)
"""