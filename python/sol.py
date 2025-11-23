class Solution:
    def main(self, s: str, t: str) -> bool:
        if not s:
            return True

        i = 0
        for char in t:
            if s[i] == char:
                i += 1
                if i == len(s):
                    return True

        return False

if __name__ == "__main__":
    sol = Solution()
    print(sol.main("abc", "ahbgdc"))  # Output: True
    print(sol.main("axc", "ahbgdc"))  # Output: False