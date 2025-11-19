"""
LeetCode Problem: 2091. Removing Minimum and Maximum From Array

Algorithm: Find indices of min and max, calculate deletions from front, back, and both sides.

Time Complexity: O(n) to find min and max -> O(n)

Space Complexity: O(1) for variables -> O(1)
"""

class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        max_value = max(nums)
        min_value = min(nums)
        max_index = max(nums.index(max_value), nums.index(min_value))
        min_index = min(nums.index(max_value), nums.index(min_value))

        # from front
        front = max_index + 1

        # from back
        back = n - min_index

        # from both side
        mix1 = (min_index + 1) + (n - max_index)
        mix2 = (max_index + 1) + (n - min_index)

        return min(front, back, mix1, mix2)
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.minimumDeletions([2,10,7,5,4,1,8,6]))  # Output: 5
    print(sol.minimumDeletions([0,-4,19,1,8,-2,-3,5]))  # Output: 3
    print(sol.minimumDeletions([101]))  # Output: 1


"""
Optimization: Do in one pass to find min and max indices. -> O(n) time, O(1) space.

Final Version ->
class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        min_index, max_index = 0, 0

        for i, val in enumerate(nums):
            if val < nums[min_index]:
                min_index = i
            if val > nums[max_index]:
                max_index = i

        left, right = min(min_index, max_index), max(min_index, max_index)

        front = right + 1
        back = n - left
        both1 = (left + 1) + (n - right)
        both2 = (right + 1) + (n - left)

        return min(front, back, both1, both2)

Time Complexity: O(n)

Space Complexity: O(1)
"""