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