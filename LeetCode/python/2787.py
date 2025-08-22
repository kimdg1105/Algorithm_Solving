class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        print(self.findFirst(n, x))
        return 0

    def findFirst(self, n: int, x: int) -> int:
        low, high = 1, 300
        while low <= high:
            mid = (low + high) // 2
            cal = mid**x
            if n < cal:
                high = mid
            else:
                return mid
        return low


Solution().numberOfWays(10, 2)  # 1
Solution().numberOfWays(4, 1)  # 2
