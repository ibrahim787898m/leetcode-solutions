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