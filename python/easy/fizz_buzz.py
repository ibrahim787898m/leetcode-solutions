"""
LeetCode Problem: 412. Fizz Buzz

Algorithm: Check divisibility for each number and append corresponding string.

Time Complexity: Loop runs n times, constant work for each iteration -> O(n)

Space Complexity: List res stores n strings -> O(n)
"""

class Solution(object):
    def fizzBuzz(self, n):
        res = []
        
        for i in range(1, n + 1):
            if i % 15 == 0:
                res.append("FizzBuzz")
            elif i % 5 == 0:
                res.append("Buzz")
            elif i % 3 == 0:
                res.append("Fizz")

            else:
                res.append(str(i))
        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.fizzBuzz(3))   # ["1","2","Fizz"]
    print(sol.fizzBuzz(5))   # ["1","2","Fizz","4","Buzz"]
    print(sol.fizzBuzz(15))  # ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

"""
Optimization: Use List Comprehension for conciseness and efficiency. Also uses type hints for clarity. -> O(n) time, O(n) space.

Final Version ->
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return [
        ("Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0)) or str(i) for i in range(1, n + 1)]

Time Complexity: O(n)

Space Complexity: O(n)
"""