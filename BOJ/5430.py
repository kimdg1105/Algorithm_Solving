from collections import deque

class AC(object):

    def __init__(self, data, cmd):
        self.data = deque()
        self.cmd = cmd
        for d in data:
            if d != '':
                self.data.append(d)


    def stats(self):
        print("MY DATA", self.data, self.cmd)

    def R(self):
        self.data.reverse()
        return

    def D(self,paze):
        if self.data:
            if paze == 1:
                self.data.popleft()
            if paze == 0:
                self.data.pop()
        else:
            return 1



    def solve(self):
        cmd = self.cmd
        r_cnt = 0
        for c in cmd:
            if c == 'R':
                r_cnt +=1
                continue

            if c == 'D':
                if r_cnt % 2 == 0:
                    paze = 1
                else:
                    paze = 0

                if self.D(paze) == 1:
                    self.data = 'error'
                    break

        if self.data == 'error':
            print(self.data)
        else:
            if r_cnt % 2 != 0:
                self.R()
            print('[', end='')
            print(*self.data, sep=',', end='')
            print(']')


T = int(input())
for _ in range(T):
    p = str(input())
    n = int(input())
    arr = input()
    arr = arr[1:-1].split(',')

    myAC = AC(data=arr, cmd=p)
    # myAC.stats()
    myAC.solve()
