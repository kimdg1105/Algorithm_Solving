n = int(input())

arr = map(int, input().split(" "))

v = int(input())

cnt = 0

for val in arr:
    if val == v:
        cnt += 1

print(cnt)
