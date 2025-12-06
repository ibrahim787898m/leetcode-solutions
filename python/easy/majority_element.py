"""
LeetCode Problem: 169. Majority Element

Algorithm: Hash map to count occurrences of each element.

Time Complexity: O(n) where n is the length of nums -> O(n)

Space Complexity: O(n) for the hash map -> O(n)
"""

class Solution(object):
    def majorityElement(self, nums):
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        max_key = max(count, key=count.get)
        return max_key
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.majorityElement([3,2,3]))  # 3
    print(sol.majorityElement([2,2,1,1,1,2,2]))  # 2

"""
Optimization: Boyer-Moore Voting Algorithm for O(n) time and O(1) space. -> O(n) time, O(1) space

Final Version ->
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
            elif num == candidate:
                count += 1
            else:
                count -= 1

        return candidate

Time Complexity: O(n) where n is the length of nums -> O(n)

Space Complexity: O(1) for storing candidate and count -> O(1)
"""