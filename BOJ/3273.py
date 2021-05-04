import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int,input().split()))
target = int(input())
ret = 0
cnt = 0
start, end = 0, N-1


num_list.sort()
while start != end:
    if num_list[start] + num_list[end] > target:
        end -= 1
    elif num_list[start] + num_list[end] < target:
        start +=1
    else:

        cnt += 1
        start +=1

print(cnt)