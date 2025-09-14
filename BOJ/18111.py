import sys


n, m, b = map(int, input().split())

land = []
for _ in range(n):
    land.append(list(map(int, input().split())))


low = min([min(x) for x in land])
high = max([max(x) for x in land])

time = sys.maxsize
ans_lv = -1

for lv in range(low, 257):
    over = 0
    less = 0
    for i in range(n):
        for j in range(m):
            if land[i][j] >= lv:
                over += land[i][j] - lv
            else:
                less += lv - land[i][j]

    if over + b >= less:
        if over * 2 + less <= time:
            time = over * 2 + less
            ans_lv = lv

print(time, ans_lv)
