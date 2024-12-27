class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0] * n for _ in range(m)]

        grid[0][0] = 0
        grid[1][0] = 1
        grid[0][1] = 1

        def dp(x, y):
            if x >= 0 and y >= 0 and grid[x - 1][y] == 0:
                dp(x - 1, y)
            if x >= 0 and y >= 0 and grid[x][y - 1] == 0:
                dp(x, y - 1)
            grid[x][y] = grid[x][y - 1] + grid[x - 1][y]

        dp(m - 1, n - 1)
        print(grid)
        return grid[m - 1][n - 1]


Solution().uniquePaths(3, 7)
