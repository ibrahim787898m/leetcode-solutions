"""
LeetCode Problem: 2461. Maximum Sum of Distinct Subarrays of Length K

Algorithm: Sliding Window + Hash Map.

Time Complexity: O(n) where n is the length of nums -> O(n)

Space Complexity: O(k) for the hash map -> O(k)
"""

class Solution(object):
    def maximumSubarraySum(self, nums, k):
        left = 0
        right = k
        window_sum = sum(nums[:k])
        max_sum = 0
        counts = {}

        for i in range(k):
            counts[nums[i]] = counts.get(nums[i], 0) + 1

        if len(counts) == k:
            max_sum = window_sum

        while right < len(nums):
            window_sum += nums[right] - nums[left]
            counts[nums[right]] = counts.get(nums[right], 0) + 1
            counts[nums[left]] -= 1
            if counts[nums[left]] == 0:
                del counts[nums[left]]
            if len(counts) == k:
                max_sum = max(max_sum, window_sum)
            left += 1
            right += 1

        return max_sum
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.maximumSubarraySum([1,5,4,2,9,9,9], 3))  # Output: 15
    print(sol.maximumSubarraySum([4,4,4], 3))  # Output: 0

"""
Optimization: None needed, already optimal. -> O(n) time, O(k) space. Just added edge case for empty input and slightly changed variable names for clarity.

Final Version ->
class Solution(object):
    def maximumSubarraySum(self, nums, k):
        if not nums or k <= 0:
            return 0

        left = 0
        right = k

        window_sum = sum(nums[:k])
        max_sum = 0

        counts = {}

        for i in range(k):
            counts[nums[i]] = counts.get(nums[i], 0) + 1

        if len(counts) == k:
            max_sum = window_sum

        while right < len(nums):
            window_sum += nums[right] - nums[left]
            counts[nums[right]] = counts.get(nums[right], 0) + 1
            counts[nums[left]] -= 1
            if counts[nums[left]] == 0:
                del counts[nums[left]]
            if len(counts) == k:
                max_sum = max(max_sum, window_sum)
            left += 1
            right += 1

        return max_sum

Time Complexity: O(n) where n is the length of nums -> O(n)

Space Complexity: O(k) for the hash map -> O(k)
"""