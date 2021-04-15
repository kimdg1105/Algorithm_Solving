N, K = map(int,input().split())
coin = []
for _ in range(N):
    coin.append(int(input()))

coin.reverse()

idx = 0
ret = 0
while K != 0:
    if K - coin[idx] >= 0:
        r = K // coin[idx]
        K -= coin[idx]*r
        ret += r
    else:
        idx += 1

print(ret)