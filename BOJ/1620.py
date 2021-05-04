import sys
input = sys.stdin.readline

N, M = map(int, input().split())


poke = []
for i in range(N):
    poke.append(str(input().strip('\n')))

# print(poke)


for i in range(M):
    quest = str(input().strip('\n'))
    if quest.isdigit():
        print(poke[int(quest)-1])
    else:
        ans = poke.index(quest)
        print(ans+1)
