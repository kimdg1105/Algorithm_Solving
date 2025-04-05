from typing import List


class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            ret = grid[i][j]
            grid[i][j] = 0

            for k in range(4):
                cur_x, cur_y = i + dx[k], j + dy[k]
                if 0 <= cur_x < m and 0 <= cur_y < n:
                    if grid[cur_x][cur_y] != 0:
                        ret += dfs(cur_x, cur_y)
            return ret

        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        max_val = 0
        m = len(grid)
        n = len(grid[0])

        for x in range(m):
            for y in range(n):
                if grid[x][y] != 0:
                    max_val = max(max_val, dfs(x, y))
        return max_val


grid = [[0, 2, 1, 0], [4, 0, 0, 3], [1, 0, 0, 4], [0, 3, 2, 0]]

print(Solution().findMaxFish(grid))
