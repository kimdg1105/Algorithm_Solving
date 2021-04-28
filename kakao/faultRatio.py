import sys
input = sys.stdin.readline


def solution(N, stages):
    answer = []
    temp = []
    for i in range(1,N+1):
        up, down = 0,0
        for j in range(len(stages)):
            if stages[j] >= i:
                down +=1
                if stages[j] <= i:
                    up +=1
        if up == 0:
            temp.append([i,0])
        else:
            temp.append([i,up/down])

    temp.sort(key = lambda x: [-x[1],x[0]])
    print(temp)
    for i in temp:
        answer.append(i[0])
    return answer

N = int(input())
stages = list(map(int,input().split()))
ans = solution(N,stages)
print(ans)