import math
import sys

input = sys.stdin.readline

n = int(input())
dp = [0, 1]

for i in range(2, n + 1):
    minval = int(1e9)
    for j in range(1, int(math.sqrt(i)) + 1):
        minval = min(minval, dp[i - j**2] + 1)
    dp.append(minval)

print(dp[n])
