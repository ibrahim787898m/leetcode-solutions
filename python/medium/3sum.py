"""
LeetCode Problem: 15. 3Sum

Algorithm: Sorting + Two Pointers.

Time Complexity: O(n^2) where n is the length of nums -> O(n^2)

Space Complexity: O(1) ignoring the output list -> O(1)
"""

class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.threeSum([-1,0,1,2,-1,-4]))  # Output: [[-1,-1,2],[-1,0,1]]
    print(sol.threeSum([0,1,1]))  # Output: []
    print(sol.threeSum([0,0,0]))  # Output: [[0,0,0]]

"""
Optimization: None needed, already optimal. -> O(n^2) time, O(1) space. Just added edge case for empty input and slightly changed variable names for clarity.

Final Version ->
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return res

Time Complexity: O(n^2) where n is the length of nums -> O(n^2)

Space Complexity: O(1) ignoring the output list -> O(1)
"""