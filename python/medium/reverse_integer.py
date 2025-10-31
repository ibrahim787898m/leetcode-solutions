class Solution:
    def reverse(self, x):
        if x < 0:
            s = (str(x)[1:])
            rev = s[::-1]
            res = int(rev) * -1
        else:
            res = int(str(x)[::-1])

        if res < -2**31 or res > 2**31 - 1:
            return 0
        
        return res
        
if __name__ == "__main__":
    sol = Solution()
    print(sol.reverse(123))   # Output: 321
    print(sol.reverse(-123))  # Output: -321
    print(sol.reverse(120))   # Output: 21
