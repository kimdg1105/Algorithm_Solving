# 1309 동물원 S1

N = int(input())
mod = 9901
dp = [[0, 0, 0] for _ in range(N + 1)]

for i in range(3):
    dp[1][i] = 1

for i in range(2, N + 1):
    dp[i][0] = (dp[i - 1][1] + dp[i - 1][2]) % mod
    dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % mod
    dp[i][2] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]) % mod

result = (dp[N][0] + dp[N][1] + dp[N][2]) % mod
print(result)
