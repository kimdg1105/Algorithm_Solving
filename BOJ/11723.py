import sys

input = sys.stdin.readline

S = set()
for _ in range(int(input())):
    cmd = sys.stdin.readline().rsplit()

    if cmd[0] == 'add':
        S.add(int(cmd[1]))
    elif cmd[0] == 'remove':
        if int(cmd[1]) in S:
            S.remove(int(cmd[1]))
    elif cmd[0] == 'check':
        if int(cmd[1]) in S:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'toggle':
        if int(cmd[1]) in S:
            S.remove(int(cmd[1]))
        else:
            S.add(int(cmd[1]))
    elif cmd[0] == 'all':
        S = set(range(1, 21))
    elif cmd[0] == 'empty':
        S.clear()