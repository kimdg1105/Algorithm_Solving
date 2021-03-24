# 11057 오르막 수

N = int(input())

dp = [[0 for _ in range(10)] for _ in range(N + 1)]
dp[1] = [1 for _ in range(10)]

for i in range(2, N + 1):
    for j in range(10):
        for k in range(j, 10):
            dp[i][j] += dp[i - 1][k]

result = sum(dp[N]) % 10007
print(result)
