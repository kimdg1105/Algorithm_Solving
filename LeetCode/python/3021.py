class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        ans = n * m // 2

        return ans


print(Solution().flowerGame(3, 2))
print(Solution().flowerGame(1, 1))
print(Solution().flowerGame(58280, 69389))
