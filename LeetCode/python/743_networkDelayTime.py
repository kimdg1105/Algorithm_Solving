from collections import defaultdict
import heapq
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        values = {}
        hq = []
        graph = defaultdict(list)
        for i, j, weight in times:
            graph[i].append((weight, j))

        start = (0, k)
        heapq.heappush(hq, start)

        while hq:
            cur_weight, cur_node = heapq.heappop(hq)
            if cur_node not in values:
                values[cur_node] = cur_weight
                for next_weight, next_node in graph[cur_node]:
                    heapq.heappush(hq, (cur_weight + next_weight, next_node))

        max_weight = -1
        if len(values) != n:
            return max_weight
        for node, total in values.items():
            max_weight = max(max_weight, total)

        return max_weight


print(Solution().networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))
