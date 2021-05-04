import sys

N = int(input())
num = [0] * N

for i in range(N):
    num[i] = int(input())

num.sort()

for i in range(N):
    print(num[i])
