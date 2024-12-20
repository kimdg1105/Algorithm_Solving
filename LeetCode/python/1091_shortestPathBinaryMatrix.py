from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0:
            return -1

        q = deque()
        ans = -1
        row, col = len(grid), len(grid[0])
        visited = [[False] * col for _ in range(row)]

        start_x, start_y = 0, 0
        dx = [0, 1, 1, 1, 0, -1, -1, -1]
        dy = [1, 1, 0, -1, -1, -1, 0, 1]
        q.append((start_x, start_y, 1))
        visited[start_x][start_y] = True

        while q:
            cur_x, cur_y, cnt = q.popleft()
            if cur_x == row - 1 and cur_y == col - 1:
                ans = cnt

            for i in range(8):
                next_x, next_y = cur_x + dx[i], cur_y + dy[i]
                if 0 <= next_x < row and 0 <= next_y < col:
                    if grid[next_x][next_y] == 0 and not visited[next_x][next_y]:
                        visited[next_x][next_y] = True
                        q.append((next_x, next_y, cnt + 1))

        return ans


sol = Solution()
grid = [[1, 0, 0], [1, 1, 0], [1, 1, 0]]
print(sol.shortestPathBinaryMatrix(grid))
