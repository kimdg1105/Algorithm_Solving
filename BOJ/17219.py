n, m = map(int, input().split())

dict = dict()
for _ in range(n):
    site, passowrd = input().split()
    dict[site] = passowrd


for _ in range(m):
    tofind = input()
    print(dict[tofind])
