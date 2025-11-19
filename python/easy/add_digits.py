"""
LeetCode Problem: 258. Add Digits

Algorithm: Repeatedly sum digits until single digit.

Time Complexity: Sum digits per iteration, few interations -> O(d)(~ O(1))

Space Complexity: String conversion each loop -> O(d)
"""

class Solution(object):
    def addDigits(self, num):
        while True:
            old = num
            new = 0
            for digit in map(int, str(old)):
                new += digit

            if new < 10:
                break
            else:
                num = new

        return new
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.addDigits(38))  # 2
    print(sol.addDigits(0))   # 0

"""
Optimization: Digital root formula: 1 + (num - 1) % 9 -> O(1) time, O(1) space.

Final Version ->
class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0

        return 1 + (num - 1) % 9

Time Complexity: O(1)

Space Complexity: O(1)
"""