
N = int(input())

g = []
dp = [0 for _ in range(N+1)]
day = 0
for i in range(N):
    t, p = map(int, input().split())
    g.append([i, t, p])

# 뒤에서부터 DP로 풀이 -> 가능한 일수가 있을 때만 pi ++
for i in range(N-1, -1, -1):
        if g[i][1] + i <= N:
            dp[i] = max(dp[i+1], g[i][2]+dp[i + g[i][1]])
        else:
            dp[i] = dp[i+1]

print(dp[0])

