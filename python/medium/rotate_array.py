"""
LeetCode Problem: 189. Rotate Array

Algorithm: Reverse the entire array, then reverse the first k elements and the rest separately.

Time Complexity: O(n) where n is the length of nums -> O(n)

Space Complexity: O(1) for in-place rotation -> O(1)
"""

class Solution(object):
    def rotate(self, nums, k):
        k %= len(nums)

        nums[:] = nums[::-1]

        nums[:k] = nums[:k][::-1]

        nums[k:] = nums[k:][::-1]

        return nums

if __name__ == "__main__":
    sol = Solution()
    print(sol.rotate([1,2,3,4,5,6,7], 3))  # [5,6,7,1,2,3,4]
    print(sol.rotate([-1,-100,3,99], 2))  # [3,99,-1,-100]

"""
Optimization: None needed, already optimal. -> O(n) time, O(1) space.
"""