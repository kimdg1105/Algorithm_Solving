from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dq = deque()
        ans = 0
        row = len(grid)
        col = len(grid[0])
        visited = [[False] * col for _ in range(row)]
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        def bfs(x: int, y: int):
            visited[x][y] = True
            dq.append((x, y))
            while dq:
                cur_x, cur_y = dq.popleft()
                for d in range(4):
                    next_x = cur_x + dx[d]
                    next_y = cur_y + dy[d]
                    if (
                        0 <= next_x < row
                        and 0 <= next_y < col
                        and grid[next_x][next_y] == "1"
                        and not visited[next_x][next_y]
                    ):
                        visited[next_x][next_y] = True
                        dq.append((next_x, next_y))

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1" and not visited[i][j]:
                    bfs(i, j)
                    ans += 1

        return ans


sol = Solution()
grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]
print(sol.numIslands(grid))
