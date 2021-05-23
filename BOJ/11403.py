N = int(input())
field = []
for _ in range(N):
    field.append(list(map(int, input().split())))

for k in range(N):
    for i in range(N):
        for j in range(N):
            if field[i][j] == 1 or (field[i][k] == 1 and field[k][j] == 1):
                field[i][j] = 1
for i in field:
    for j in i:
        print(j, end=" ")
    print()