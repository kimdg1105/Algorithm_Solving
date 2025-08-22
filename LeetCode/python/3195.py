from typing import List


class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        x, y = len(grid), len(grid[0])
        minx, maxx = x, -1
        miny, maxy = y, -1

        for i in range(x):
            for j in range(y):
                if grid[i][j] == 1:
                    minx = min(minx, i)
                    miny = min(miny, j)
                    maxx = max(maxx, i)
                    maxy = max(maxy, j)

        return (maxx - minx + 1) * (maxy - miny + 1)


print(Solution().minimumArea([[0, 1, 0], [1, 0, 1]]))
