from collections import deque


def solution(m, n, puddles):
    puddles = [[q, p] for [p, q] in puddles]
    answer = 0
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == j == 1:
                continue
            if [i, j] in puddles:
                dp[i][j] = 0

            else:
                x = dp[i - 1][j]
                y = dp[i][j - 1]

                dp[i][j] = (x + y) % 1_000_000_007

    answer = dp[-1][-1]

    return answer


print(solution(4, 3, [[2, 2]]))  # 4
print(solution(1, 3, [[1, 2]]))  # 1
