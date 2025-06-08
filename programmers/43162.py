def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]

    for pc in range(n):
        if visited[pc] == False:
            dfs(pc, visited, computers)
            answer += 1

    return answer


def dfs(pc, visited, computers):
    visited[pc] = True
    for i in range(len(visited)):
        if computers[pc][i] == 1 and visited[i] != True:
            dfs(i, visited, computers)


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
