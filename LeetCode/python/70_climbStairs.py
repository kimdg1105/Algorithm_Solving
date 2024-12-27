class Solution:
    def climbStairs(self, n: int) -> int:

        dict = {}

        dict[1] = 1
        dict[2] = 2

        for i in range(3, n + 1):
            dict[i] = dict[i - 2] + dict[i - 1] + 3

        return dict[n]


print(Solution().climbStairs(2))
