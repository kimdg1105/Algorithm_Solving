import collections


N = int(input())

field = []
for _ in range(N):
    field.append(list(map(int, input().split())))

field.sort(key=lambda x: [x[0]])

now_day = field[-1][0]
ret = []
accept = []
while now_day != 0:
    # print("now", now_day)

    while field:
        if now_day <= field[-1][0]:
            accept.append(field[-1])
            field.pop()
        else :
            break
    # print("  acc: ", accept)
    if accept:
        accept.sort(key=lambda x:x[1])
        ret.append(accept.pop())

    now_day -=1


w = 0
for i in range(len(ret)):
    w += ret[i][1]


print(w)
