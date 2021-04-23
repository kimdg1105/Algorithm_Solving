N = int(input())
w = list(map(int,input().split()))

w.sort()
check = 0
for i in range(N):
    if check +1 >= w[i]:
        check += w[i]
    else:
        break

print(check+1)