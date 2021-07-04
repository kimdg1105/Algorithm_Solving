import sys

input = sys.stdin.readline

dq = []

def push_front(X):
    dq.insert(0,X)

def push_back(X):
    dq.append(X)

def pop_front():
    try:
        print(dq.pop(0))
    except:
        print(-1)

def pop_back():
    try:
        print(dq.pop())
    except:
        print(-1)

def size():
    print(len(dq))

def empty():
    if len(dq) == 0:
        print(1)
    else:
        print(0)

def front():
    try:
        print(dq[0])
    except:
        print(-1)

def back():
    try:
        print(dq[len(dq)-1])
    except:
        print(-1)

N = int(input())

for _ in range(N):
    cmd = input().split()
    if cmd[0] == 'push_back':
        push_back(cmd[1])
    if cmd[0] == 'push_front':
        push_front(cmd[1])
    if cmd[0] == 'pop_front':
        pop_front()
    if cmd[0] == 'pop_back':
        pop_back()
    if cmd[0] == 'size':
        size()
    if cmd[0] == 'empty':
        empty()
    if cmd[0] == 'front':
        front()
    if cmd[0] == 'back':
        back()



