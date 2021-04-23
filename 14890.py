N, L = map(int, input().split())
field = []
cnt = 0

for i in range(N):
    field.append(list(map(int, input().split())))


def check(VH, linenum, L):
    global cnt
    visited = [0 for _ in range(N)]
    line = []
    if VH == 0:  # 가로
        for i in range(N):
            line.append(field[linenum][i])
    elif VH == 1:  # 세로
        for i in range(N):
            line.append(field[i][linenum])

    now_num = line[0]

    for i in range(1, N):

        if i == N - 1:
            cnt += 1
            print("ans : ",line)

        if abs(now_num - line[i]) > 1:
            break
        if now_num == line[i]:
            continue

        if now_num < line[i]:
            if 0 <= i - L < N:
                for j in range(L):
                    if line[i - j] != now_num + 1:
                        break
            else:
                break

        if now_num > line[i]:
            if 0 <= i + L < N:
                for j in range(L):
                    if line[i + j] != now_num - 1:
                        break
            else:
                break
        now_num = line[i]
    print(cnt)

    return line


ret = []

for i in range(N):
    ret.append(check(0, i, L))
    ret.append(check(1, i, L))