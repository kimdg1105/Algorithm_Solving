from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dict = {}
        dict[0] = 0
        dict[1] = 0

        for i in range(2, len(cost) + 1):
            dict[i] = min(dict[i - 2] + cost[i - 2], dict[i - 1] + cost[i - 1])
        return dict[len(cost)]


print(Solution().minCostClimbingStairs([10, 15, 20]))
print(Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
