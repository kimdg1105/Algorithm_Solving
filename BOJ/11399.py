N = int(input())

p = list(map(int, input().split()))
kp = []

for i in range(N):
    kp.append([i + 1, p[i]])

kp.sort(key=lambda x: x[1])

ret = []
temp = 0
for i in range( N):
    temp += kp[i][1]

    ret.append(temp)

print(sum(ret))

