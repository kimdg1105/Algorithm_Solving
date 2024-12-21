from collections import defaultdict
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for idx, room in enumerate(rooms):
            for key in room:
                graph[idx].append(key)

        visited = [0]
        ans = False

        def dfs(cur_room, visited):
            for can_open in graph[cur_room]:
                if can_open not in visited:
                    visited.append(can_open)
                    dfs(can_open, visited)

            if len(visited) == len(rooms):
                nonlocal ans
                ans = True
                return
            visited = []

        dfs(0, visited)
        return ans


rooms1 = [[1], [2], [3], []]
rooms2 = [[1, 3], [3, 0, 1], [2], [0]]

sol = Solution()
print(sol.canVisitAllRooms(rooms1))
print(sol.canVisitAllRooms(rooms2))
