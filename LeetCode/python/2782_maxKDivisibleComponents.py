from collections import defaultdict
from typing import List


class Solution:
    def maxKDivisibleComponents(
        self, n: int, edges: List[List[int]], values: List[int], k: int
    ) -> int:
        graph = defaultdict(list)
        for l in edges:
            graph[l[0]].append(l[1])
            graph[l[1]].append(l[0])

        ans = 0

        def dfs(cur_node, parent):
            total_sum = values[cur_node]

            for child in graph[cur_node]:
                if child != parent:
                    total_sum += dfs(child, cur_node)

            if total_sum % k == 0:
                nonlocal ans
                ans += 1
            return total_sum

        dfs(0, -1)

        return ans


sol = Solution()

print(
    sol.maxKDivisibleComponents(
        n=7,
        edges=[[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]],
        values=[3, 0, 6, 1, 5, 2, 1],
        k=3,
    )
)
