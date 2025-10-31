class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.isAnagram("anagram", "nagaram"))  # True
    print(sol.isAnagram("rat", "car"))          # False