class Solution(object):
    def isPalindrome(self, x):
        s = str(x)
        rev = s[::-1]
        # print(reversed)

        if s == rev:
            return True
        else:
            return False
        
if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome(121))  # True
    print(sol.isPalindrome(-121)) # False
    print(sol.isPalindrome(10))  # False