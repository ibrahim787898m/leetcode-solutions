"""
LeetCode Problem: 2586. Count the Number of Vowel Strings in Range

Algorithm: Loop through range, check first and last char.

Time Complexity: O(N) where N is the number of words in the given range.

Space Complexity: O(1) as we use a fixed amount of space.
"""

class Solution(object):
    def vowelStrings(self, words, left, right):

        vowels = ["a", "e", "i", "o", "u"]
        count = 0

        for i in range(left, right + 1):
            if words[i][0] in vowels and words[i][-1] in vowels:
                count += 1

        return count
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.vowelStrings(["are","amy","u"], 0, 2))  # 2
    print(sol.vowelStrings(["hey","aeo","mu","ooo","artro"], 1, 4))  # 3

"""
Optimization: Use set for vowels for O(1) lookup. -> O(1) time, O(1) space.

Final Version ->
class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        vowels = set("aeiou")
        return sum(word[0] in vowels and word[-1] in vowels for word in words[left:right+1])

Time Complexity: O(N)

Space Complexity: O(1)
"""