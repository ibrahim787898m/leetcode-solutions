"""
LeetCode Problem: 268. Missing Number

Algorithm: Set-based lookup.

Time Complexity: O(n) where n is the length of nums -> O(n)

Space Complexity: O(n) for the set -> O(n)
"""

class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        num_set = set(nums)

        for char in range(n + 1):
            if char not in num_set:
                return char
            
if __name__ == "__main__":
    sol = Solution()
    print(sol.missingNumber([3,0,1]))  # Output: 2
    print(sol.missingNumber([0,1]))    # Output: 2
    print(sol.missingNumber([9,6,4,2,3,5,7,0,1]))  # Output: 8

"""
Optimization: Mathematical formula for O(1) space and O(n) time. -> O(n) time, O(1) space.

Final Version ->
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum

Time Complexity: O(n) where n is the length of nums -> O(n)

Space Complexity: O(1) for storing sums -> O(1)
"""