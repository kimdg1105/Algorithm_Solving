n = int(input())


dict = {}
for _ in range(n):
    x, y = map(int, input().split())
    if x not in dict:
        dict[x] = []
    dict[x].append(y)

key_sorted = sorted(dict)

for key in key_sorted:
    dict[key].sort()
    for v in dict[key]:
        print(key, v)
