"""
LeetCode Problem: 217. Contains Duplicate

Algorithm: Hash map with frequency count.

Time Complexity: O(n) where n is the length of nums -> O(n)

Space Complexity: O(n) for the hash map -> O(n)
"""

class Solution(object):
    def containsDuplicate(self, nums):
        seen = {}
        bool = False

        for num in nums:
            seen[num] = seen.get(num, 0) + 1
            if seen.get(num) > 1:   #type: ignore
                bool = True
            
        return bool
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.containsDuplicate([1,2,3,1]))  # True
    print(sol.containsDuplicate([1,2,3,4]))  # False
    print(sol.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))  # True

"""
Optimization: Hash set with early return on duplicate detection -> O(n) time, O(n) space.

Final Version ->
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False

Time Complexity: O(n) where n is the length of nums -> O(n)

Space Complexity: O(n) for the hash set -> O(n)
"""