"""
LeetCode Problem: 202. Happy Number

Algorithm: Hash set Cycle Detection.

Time Complexity: O(log n) where n is the input number -> O(log n)

Space Complexity: O(log n) for the set -> O(log n)
"""

class Solution(object):
    def isHappy(self, n):
        seen = set()

        while n != 1:
            if n in seen:
                return False
            
            seen.add(n)

            total = 0
            for digit in str(n):
                total += int(digit) ** 2

            n = total

        return True
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.isHappy(19))  # True
    print(sol.isHappy(2))   # False

"""
Optimization: Floyd's Cycle Detection Algorithm for O(1) space. -> O(log n) time, O(1) space.

Final Version -> 
class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(num):
            total = 0
            while num > 0:
                digit = num % 10
                total += digit ** 2
                num //= 10
            return total

        slow = n
        fast = get_next(n)

        while fast != 1 and slow != fast:
            slow = get_next(slow)
            fast = get_next(get_next(fast))

        return fast == 1

Time Complexity: O(log n) where n is the input number -> O(log n)

Space Complexity: O(1) for the two pointers -> O(1)
"""
