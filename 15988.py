# 15988 1, 2, 3 더하기 3


mod = 1000000009
case = int(input())
dp = [0] * 1000001
dp[1], dp[2], dp[3] = 1, 2, 4

for i in range(4, 1000001):
    dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % mod


for _ in range(case):
    N = int(input())
    print(dp[N])
