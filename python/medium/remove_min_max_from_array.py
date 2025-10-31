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