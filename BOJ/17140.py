


r,c,k = map(int,input().split())

A = []
for _ in range(3):
    A.append(list(map(int,input().split())))


def rcal(matrix):
    maxlen = 0
    for i in range(len(matrix)):
        dict = {}
        for j in matrix[i]:
            if j == 0:
                continue
            if j in dict:
                dict[j] += 1
            else:
                dict[j] = 1
        temp = sorted(dict.items(),key=lambda x :(x[1],x[0]))
        line = []
        for k in temp:
            line.append(k[0])
            line.append(k[1])
        matrix[i] = line
        maxlen = max(maxlen, len(matrix[i]))

    for i in range(len(matrix)):
        while len(matrix[i]) != maxlen and len(matrix[i]) <= 100:
            matrix[i].append(0)


row_len = 0
col_len = 0
cnt = 0
while True:
    if len(A) > r - 1 and len(A[0]) > c - 1:
        if A[r - 1][c - 1] == k:
            print(cnt)
            break

    if cnt >= 100:
        print(-1)
        break

    row_len = len(A)
    col_len = len(A[0])

    if row_len >= col_len:
        rcal(A)
    else:
        A = list(map(list, zip(*A)))
        rcal(A)
        A = list(map(list, zip(*A)))
    cnt += 1

    # for l in A:
    #     print(l)
    # print("----")


