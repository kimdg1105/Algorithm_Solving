class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        ans = 0
        rx = abs(z - x)
        ry = abs(z - y)

        if rx > ry:
            ans = 2
        elif rx < ry:
            ans = 1
        else:
            ans = 0

        return ans


print(Solution().findClosest(2, 7, 4))
