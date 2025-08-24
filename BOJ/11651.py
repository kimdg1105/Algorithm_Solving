n = int(input())
arr = []
for _ in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))

arr.sort(key=lambda v: (v[1], v[0]))


for tuple in arr:
    print(str(tuple[0]) + " " + str(tuple[1]))
