n = int(input())

human = []
arr = [1] * n
for _ in range(n):
    x, y = map(int, input().split())
    human.append((x, y))

for i in range(n):
    for j in range(n):
        if i == j:
            continue

        if human[i][0] < human[j][0] and human[i][1] < human[j][1]:
            arr[i] += 1


print(" ".join(map(str, arr)))
