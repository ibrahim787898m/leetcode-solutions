class Solution(object):
    def vowelStrings(self, words, left, right):

        vowels = ["a", "e", "i", "o", "u"]
        count = 0

        for i in range(left, right + 1):
            if words[i][0] in vowels and words[i][-1] in vowels:
                count += 1

        return count
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.vowelStrings(["are","amy","u"], 0, 2))  # 2
    print(sol.vowelStrings(["hey","aeo","mu","ooo","artro"], 1, 4))  # 3