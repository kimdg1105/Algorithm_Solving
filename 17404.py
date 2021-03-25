import sys

INF = sys.maxsize

N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]

ans = INF

for color in range(3):
    dp = [[0, 0, 0] for _ in range(N)]

    for i in range(3):
        if color == i:
            dp[0][i] = cost[0][i]
        else:
            dp[0][i] = INF

    for i in range(1, N):
        dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + cost[i][0]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + cost[i][1]
        dp[i][2] = min(dp[i - 1][1], dp[i - 1][0]) + cost[i][2]

    for i in range(3):
        if color == i:
            continue
        ans = min(ans, dp[N - 1][i])


print(ans)
