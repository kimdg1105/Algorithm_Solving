from collections import deque

topni = []
topni.append(deque([-1, -1, -1, -1, -1, -1, -1, -1]))

for _ in range(4):
    tn = list(map(int, str(input())))
    d = deque(tn)
    topni.append(d)

K = int(input())
cmd = []
for _ in range(K):
    cmd.append(list(map(int, input().split())))


def check_left(tnum, paze):
    if tnum <= 1 or  topni[tnum][6] == topni[tnum - 1][2]:
        return

    if topni[tnum][6] != topni[tnum - 1][2]:
        # print("spin left", tnum-1)
        check_left(tnum - 1, paze * -1)
        spin(tnum - 1, paze * -1)



def check_right(tnum, paze):
    if tnum >= 4 or topni[tnum][2] == topni[tnum + 1][6]:
        return

    if topni[tnum][2] != topni[tnum + 1][6]:
        # print("spin right", tnum)
        check_right(tnum + 1, paze * -1)
        spin(tnum + 1, paze * -1)



def spin(tnum, paze):
    if paze == 1:
        topni[tnum].rotate(1)

    elif paze == -1:
        topni[tnum].rotate(-1)


for c in cmd:
    check_left(c[0], c[1])
    check_right(c[0], c[1])
    spin(c[0], c[1])

ret = 0
if topni[1][0] == 1:
    ret += 1
elif topni[1][0] == 0:
    ret += 0
if topni[2][0] == 1:
    ret += 2
elif topni[2][0] == 0:
    ret += 0
if topni[3][0] == 1:
    ret += 4
elif topni[3][0] == 0:
    ret += 0
if topni[4][0] == 1:
    ret += 8
elif topni[4][0] == 0:
    ret += 0

print(ret)
