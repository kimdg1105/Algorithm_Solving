import sys


input = sys.stdin.readline

n, m = map(int, input().split())

arr = list(map(int, input().split()))
cumul_arr = [0] * (len(arr) + 1)

for idx, val in enumerate(arr):
    cumul_arr[idx + 1] = cumul_arr[idx] + val

for _ in range(m):
    start, end = map(int, input().split())
    ret = cumul_arr[end] - cumul_arr[start - 1]
    print(ret)
