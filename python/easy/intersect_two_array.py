"""
LeetCode Problem: 349. Intersection of Two Arrays

Algorithm: Use sets to find common elements.

Time Complexity: O(n + m) where n and m are the lengths of nums1 and nums2 -> O(n + m)

Space Complexity: O(n) for storing elements of nums1 in a set -> O(n)
"""

class Solution(object):
    def intersection(self, nums1, nums2):
        seen = set(nums1)

        res = set()

        for num in nums2:
            if num in seen:
                res.add(num)

        res = list(res)

        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.intersection([1,2,2,1], [2,2]))  # [2]
    print(sol.intersection([4,9,5], [9,4,9,8,4]))  # [9,4]

"""
Optimization: Use set intersection for more concise code. -> O(n + m) time, O(n) space.

Final Version ->
class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        return list(set(nums1) & set(nums2))

Time Complexity: O(n + m) where n and m are the lengths of nums1 and nums2 -> O(n + m)

Space Complexity: O(n) for storing elements of nums1 in a set -> O(n)
"""