import sys
N = int(input())

field = []
for _ in range(N):
    field.append(list(map(int, input().split())))

field.sort(key= lambda x : (x[1], x[0]))

time = 0
ret = []
for i in range(N):
    if time <= field[i][0]:
        ret.append(field[i])
        time = field[i][1]


print(len(ret))