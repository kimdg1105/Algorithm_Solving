import sys

N = int(input())

cost = list(map(int, input().split()))
price = list(map(int, input().split()))

ret = 0
minprice = sys.maxsize
for i in range(N - 1):
    if i == 0:
        ret += cost[i] * price[i]
        minprice = price[i]
    else:
        if price[i] < minprice:
            minprice = price[i]
        ret += cost[i] * minprice


print(ret)
