n, m, b = map(int, input().split())

land = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    raw = list(map(int, input().split()))
    land[i] = raw

print(land)
print(n, m, b)
