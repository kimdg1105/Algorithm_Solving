import itertools
import sys

N = int(input())

hp = list(map(int, input().split()))
while len(hp) != 3:
    hp.append(0)


dp = [[[-1 for _ in range(61)] for _ in range(61)] for _ in range(61)]


def solve(a, b, c):

    if a < 0:
        return solve(0, b, c)
    if b < 0:
        return solve(a, 0, c)
    if c < 0:
        return solve(a, b, 0)
    if a <= 0 and b <= 0 and c <= 0:
        return 0

    if dp[a][b][c] != -1:
        return dp[a][b][c]

    cnt = sys.maxsize
    for case in list(itertools.permutations([1, 3, 9])):
        cnt = min(cnt, solve(a - case[0], b - case[1], c - case[2]))
    dp[a][b][c] = cnt + 1
    return dp[a][b][c]


print(solve(hp[0], hp[1], hp[2]))
