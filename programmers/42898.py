from collections import deque


def solution(m, n, puddles):
    answer = 0
    matrix = [[0] * m for _ in range(n)]
    for puddle in puddles:
        x, y = puddle
        matrix[y - 1][x - 1] = 1

    start_x, start_y = 0, 0
    dx = [0, 1]
    dy = [1, 0]

    q = deque()
    q.append((start_x, start_y))

    while q:
        x, y = q.popleft()
        for i in range(2):
            cur_x, cur_y = x + dx[i], y + dy[i]
            if cur_x == n - 1 and cur_y == m - 1:
                answer += 1
            if 0 <= cur_x < n and 0 <= cur_y < m:
                if matrix[cur_x][cur_y] == 0:
                    q.append((cur_x, cur_y))

    return answer % 1_000_000_007


print(solution(4, 3, [[2, 2]]))  # 4
