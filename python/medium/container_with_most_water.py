"""
LeetCode Problem: 11. Container With Most Water

Algorithm: Two Pointers Greedy approach.

Time Complexity: O(n) where n is the length of height -> O(n)

Space Complexity: O(1) -> O(1)
"""

class Solution(object):
    def maxArea(self, height):
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            max_area = max(max_area, (right - left) * min(height[left], height[right]))

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxArea([1,8,6,2,5,4,8,3,7]))  # Output: 49
    print(sol.maxArea([1,1]))  # Output: 1

"""
Optimization: None needed, already optimal. -> O(n) time, O(1) space. Just added edge case for empty input. And slightly changed variable names for clarity.

Final Version ->
class Solution(object):
    def maxArea(self, height):
        if not height:
            return 0

        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            width = right - left
            current_area = width * min(height[left], height[right])
            max_area = max(max_area, current_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

Time Complexity: O(n) where n is the length of height -> O(n)

Space Complexity: O(1) -> O(1)
"""