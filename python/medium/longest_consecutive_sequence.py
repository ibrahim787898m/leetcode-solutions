"""
LeetCode Problem: 128. Longest Consecutive Sequence

Algorithm: Smart Hash Set approach.

Time Complexity: O(n) where n is the length of nums -> O(n)

Space Complexity: O(n) for the hash set -> O(n)
"""

class Solution(object):
    def longestConsecutive(self, nums):
        num_set = set(nums)
        length = 0

        for num in num_set:
            if (num - 1) not in num_set:
                count = 1
                current = num

                while (current + 1) in num_set:
                    count += 1
                    current += 1

                length = max(length, count)

        return length
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.longestConsecutive([100, 4, 200, 1, 3, 2]))  # Output: 4
    print(sol.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))  # Output: 9
    print(sol.longestConsecutive([1,2,0,1]))  # Output: 3

"""
Optimization: None needed, already optimal. -> O(n) time, O(n) space. Just add edge case for empty input. And change variable names.
Slightly cleaner final version ->
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0

        num_set = set(nums)
        max_length = 0

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_length = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1

                max_length = max(max_length, current_length)

        return max_length

Time Complexity: O(n) where n is the length of nums -> O(n)

Space Complexity: O(n) for the hash set -> O(n)
"""