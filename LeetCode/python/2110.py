from collections import defaultdict
from typing import List


class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        res = 0
        prev = 1

        for i in range(n):
            if i == 0:
                res = 1
                continue
            if prices[i] == prices[i - 1] - 1:
                prev += 1
            else:
                prev = 1
            res += prev

        return res


print(Solution().getDescentPeriods([3, 2, 1, 4]))
print(Solution().getDescentPeriods([8, 6, 7, 7]))
print(Solution().getDescentPeriods([1]))
