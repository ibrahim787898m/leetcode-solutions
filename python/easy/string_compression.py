"""
LeetCode Problem: 443. String Compression

Algorithm: Two-pointer technique to compress in-place.

Time Complexity: O(n) where n is the length of chars -> O(n)

Space Complexity: O(1) for in-place compression -> O(1)
"""

class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        
        i = 0
        write = 0

        while i < len(chars):
            char = chars[i]
            count = 0
            while i < len(chars) and chars[i] == char:
                i += 1
                count += 1
            chars[write] = char
            write += 1
            if count > 1:
                for c in str(count):
                    chars[write] = c
                    write += 1

        return write
        
if __name__ == "__main__":
    sol = Solution()
    print(sol.compress(["a","a","b","b","c","c","c"]))  # 6
    print(sol.compress(["a"]))                            # 1
    print(sol.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))  # 4

"""
Optimization: More explicit variable names for clarity. -> O(n) time, O(1) space.

Final Version ->
class Solution:
    def compress(self, chars: List[str]) -> int:
        read = 0
        write = 0

        while read < len(chars):
            current_char = chars[read]
            count = 0
            
            while read < len(chars) and chars[read] == current_char:
                read += 1
                count += 1

            chars[write] = current_char
            write += 1

            if count > 1:
                for digit in str(count):
                    char[write] = digit
                    write += 1

        return write

Time Complexity: O(n)

Space Complexity: O(1)
"""