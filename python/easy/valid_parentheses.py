"""
LeetCode Problem: 20. Valid Parentheses

Algorithm: Stack to match opening and closing brackets.

Time Complexity: O(n) where n is the length of the string -> O(n)

Space Complexity: O(n) for the stack in worst case -> O(n)
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        mapping = {")": "(", "}": "{", "]": "["}

        stack = []

        for char in s:
            if char in mapping.values():
                stack.append(char)
            else:
                if not stack or stack.pop() != mapping[char]:
                    return False

        return not stack
        
if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid("()"))          # True
    print(sol.isValid("()[]{}"))      # True
    print(sol.isValid("(]"))          # False
    print(sol.isValid("([])"))        # True
    print(sol.isValid("([)]"))        # False

"""
Optimization: Inverted logic. check closing first, else opening (O(1) lookup instead of O(3) values search) -> O(n) time, O(n) space.

Final Version ->
class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {")": "(", "}": "{", "]": "["}
        stack = []

        for char in s:
            if char in mapping:
                if not stack or stack.pop() != mapping[char]:
                    return False
            else:
                stack.append(char)

        return not stack

Time Complexity: O(n)

Space Complexity: O(n)
"""