class Solution(object):
    def isPalindrome(self, s):
        s = ''.join(ch for ch in s if ch.isalnum())
        s = s.lower()

        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False

            left += 1
            right -= 1
            
        return True
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome("A man, a plan, a canal: Panama"))  # True
    print(sol.isPalindrome("race a car"))                      # False
    print(sol.isPalindrome(" "))                                # True