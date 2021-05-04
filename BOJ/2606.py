n = int(input())
connect = int(input())
l = []
for _ in range(connect):
    l.append(list(map(int,input().split())))

virus = [1]

for i in range(1, n):
    for j in range(len(l)):
        if i in virus:
            if l[j][0] == i:
                virus.append(l[j][1])
            elif l[j][1] == i:
                virus.append(l[j][0])

v = set(virus)

print(len(v)-1)