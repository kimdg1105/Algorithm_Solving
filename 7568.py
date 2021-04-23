import sys
input = sys.stdin.readline

N = int(input())
member = [[0,0,0]]
for i in range(N):
    kg, height = map(int, input().split())
    member.append([i,kg,height])

rank = 0
member.sort(key= lambda x: [x[1], x[2]], reverse=True)

ret = []
for i in range(N):
    if member[i][1] > member[i+1][1] and member[i][2] > member[i+1][2]:
        rank = i + 1
        ret.append([member[i],rank])
        rank +=1

    else:
        ret.append([member[i], rank])




print(member)
print("ans:")
print(ret)