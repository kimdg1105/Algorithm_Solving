from collections import deque


t = int(input())


def make_num(n: int):
    str_n = str(n)
    while len(str_n) != 4:
        str_n = "0" + str_n
    return str_n


def d(n: int):
    ans = 2 * n
    if ans > 9999:
        ans = ans % 10000

    return ans


def s(n: int):
    ans = 0
    if n == 0:
        ans = 9999
    else:
        ans = n - 1
    return ans


def l(n: int):
    str_n = make_num(n)
    d1, d2, d3, d4 = str_n[0], str_n[1], str_n[2], str_n[3]
    str_ans = d2 + d3 + d4 + d1
    return int(str_ans)


def r(n: int):
    str_n = make_num(n)
    d1, d2, d3, d4 = str_n[0], str_n[1], str_n[2], str_n[3]
    str_ans = d4 + d1 + d2 + d3
    return int(str_ans)


def reg():
    a, b = map(int, input().split())
    q = deque()
    vistied = {a: ""}
    q.append(a)

    while q:
        cur = q.popleft()

        if cur == b:
            break

        nd = d(cur)
        if nd not in vistied:
            q.append(nd)
            vistied[nd] = vistied[cur] + "D"
        ns = s(cur)
        if ns not in vistied:
            q.append(ns)
            vistied[ns] = vistied[cur] + "S"
        nl = l(cur)
        if nl not in vistied:
            q.append(nl)
            vistied[nl] = vistied[cur] + "L"
        nr = r(cur)
        if nr not in vistied:
            q.append(nr)
            vistied[nr] = vistied[cur] + "R"

    print(vistied[b])


for _ in range(t):
    reg()
