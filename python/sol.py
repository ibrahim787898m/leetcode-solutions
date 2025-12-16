class Solution:
    def main(self, n: int) -> int:
        result = 1 
        for i in range(1, n + 1):
            result *= i
        return result
        
                
        
if __name__ == "__main__":
    sol = Solution()
    print(sol.main(2))
    print(sol.main(3))
    print(sol.main(4))
    print(sol.main(5))
   