"""
LeetCode Problem: 283. Move Zeroes

Algorithm: Iterate through the list, remove zeros and append them at the end.

Time Complexity: O(n^2) in worst case due to list.remove() being O(n) inside a loop -> O(n^2)

Space Complexity: O(1) as it modifies the list in place -> O(1)
"""

class Solution(object):
    def moveZeroes(self, nums):
        for num in nums:
            if num == 0:
                nums.remove(num)
                nums.append(0)

        return nums
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.moveZeroes([0,1,0,3,12]))  # [1,3,12,0,0]
    print(sol.moveZeroes([0]))  # [0]
    print(sol.moveZeroes([1, 0, 0, 2]))  # [1,2,0,0]

"""
Optimization: Two-pointer technique to achieve O(n) time complexity. -> O(n) time, O(1) space.

Final Version ->
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        i = 0  # Pointer for the position of the next non-zero element
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        return nums

Time Complexity: O(n) where n is the length of nums -> O(n)

Space Complexity: O(1) as it modifies the list in place -> O(1)
"""