from collections import deque


def solution(nodes, edges):
    answer = [0, 0]
    visited = set()

    my_dict = {}
    for node in nodes:
        my_dict[node] = []
    for edge in edges:
        my_dict[edge[0]].append(edge[1])
        my_dict[edge[1]].append(edge[0])

    def bfs(node, visited):
        if node in visited:
            return None

        q = deque()
        yellow, red = 0, 0

        q.append(node)

        while q:
            now = q.pop()
            visited.add(now)

            now_edge = len(my_dict[now]) - 1

            if now % 2 == 0:
                if now_edge % 2 == 0:
                    yellow += 1
                else:
                    red += 1
            else:
                if now_edge % 2 == 0:
                    red += 1
                else:
                    yellow += 1

            for next in my_dict[now]:
                if next not in visited:
                    q.append(next)

        return yellow, red

    for node in nodes:
        common, reverse = False, False

        ans = bfs(node, visited)
        if ans != None:
            if ans[0] == 1:
                answer[1] += 1
            if ans[1] == 1:
                answer[0] += 1

    return answer


# [1, 0]
print(solution([11, 9, 3, 2, 4, 6], [[9, 11], [2, 3], [6, 3], [3, 4]]))

# [2, 1]
print(
    solution(
        [9, 15, 14, 7, 6, 1, 2, 4, 5, 11, 8, 10],
        [[5, 14], [1, 4], [9, 11], [2, 15], [2, 5], [9, 7], [8, 1], [6, 4]],
    )
)
