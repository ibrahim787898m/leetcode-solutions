# class Solution:
#     def main(self, nums, k):
#         left = 0
#         right = k
#         window_sum = sum(nums[:k])
#         max_sum = window_sum
#         seen = set(nums[:k])

#         while right < len(nums):
#             seen.discard(nums[left])
        
                
        
# if __name__ == "__main__":
#     sol = Solution()
#     print(sol.main([1, 5, 4, 2, 9, 9, 9], 3))  # Example usage


# s = "AABABBA"
# k = 1
# left = 0
# right = 0
# max_count = 0
# count = {}

# while right < len(s):
#     count[s[right]] = count.get(s[right] , 0) + 1
#     max_count = max(max_count, count[s[right]])

#     if right - left + 1 - max_count > k:
#         count[s[left]] -= 1
#         left += 1

#     right += 1

# print(right - left)

nums = [1,2,3,4,5]
n = len(nums)
print(n)

sum = n * (n + 1) // 2

print(sum)  # Output: 15