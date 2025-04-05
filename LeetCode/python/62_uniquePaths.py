class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0] * n for _ in range(m)]

        if m == 1 or n == 1:
            return 1

        for r in range(m):
            grid[r][0] = 1

        for c in range(n):
            grid[0][c] = 1

        def dp(x, y):
            if x >= 0 and y >= 0 and grid[x - 1][y] == 0:
                dp(x - 1, y)
            if x >= 0 and y >= 0 and grid[x][y - 1] == 0:
                dp(x, y - 1)
            grid[x][y] = grid[x][y - 1] + grid[x - 1][y]

        dp(m - 1, n - 1)
        return grid[m - 1][n - 1]


print(Solution().uniquePaths(1, 2))
