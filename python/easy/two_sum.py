"""
LeetCode Problem: 1. Two Sum

Algorithm: Brute-force nested loops to find the pair.

Time Complexity: O(n^2) where n is the length of nums -> O(n^2)

Space Complexity: O(1) for storing indices -> O(1)
"""

class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i, j
                
if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2,7,11,15], 9))   # [0, 1]
    print(sol.twoSum([3,2,4], 6))       # [1, 2]
    print(sol.twoSum([3,3], 6))         # [0, 1]

"""
Optimization: Use a hash map to store complements for O(n) time complexity.

Final Version ->
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_map = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in num_map:
                return [num_map[comp], i]
            num_map[num] = i
        return []

Time Complexity: O(n) where n is the length of nums -> O(n)

Space Complexity: O(n) for the hash map -> O(n)
"""