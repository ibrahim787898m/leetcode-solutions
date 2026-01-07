"""
LeetCode Problem: 42. Trapping Rain Water

Algorithm: Two Pointers approach.

Time Complexity: O(n) where n is the length of height -> O(n)

Space Complexity: O(1) -> O(1)
"""

class Solution(object):
    def trap(self, height):
        water = 0
        left = 0
        right = len(height) - 1
        left_max = 0
        right_max = 0

        while left < right:
            if height[left] <= height[right]:
                left_max = max(left_max, height[left])
                water += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                water += right_max - height[right]
                right -= 1

        return water
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]))  # Output: 6
    print(sol.trap([4,2,0,3,2,5]))  # Output: 9

"""
Optimization: None needed, already optimal. -> O(n) time, O(1) space. Just added edge case for empty input. And slightly changed variable names for clarity.

Final Version ->
class Solution(object:
    def trap(self, height):
        if not height:
            return 0

        water = 0
        left = 0
        right = len(height) - 1
        left_max = 0
        right_max = 0

        while left < right:
            if height[left] <= height[right]:
                left_max = max(left_max, height[left])
                water += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                water += right_max - height[right]
                right -= 1

        return water

Time Complexity: O(n) where n is the length of height -> O(n)

Space Complexity: O(1) -> O(1)
"""