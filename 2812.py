# from itertools import combinations
#
# N, K = map(int,input().split())
# number = str(input())
#
#
# idx = []
# print(number[0],number[1])
# for i in range(N):
#     idx.append(i)
#
# comb = list(combinations(idx, K))
#
# rm_list = []
# for i in range(len(comb)):
#     add = []
#     for j in range(len(str(number))):
#         if str(j) not in str(comb[i]):
#             add.append(number[j])
#     rm_list.append(add)
#
# for i in range(len(rm_list)):
#     num = 0
#     st = 0
#     for j in range(len(rm_list[i])-1, -1, -1):
#         num += rm_list[i][j] * pow(10, st)
#         st += 1
#     rm_list[i] = num
#
# print(max(rm_list))

N, K = map(int, input().split())
value = str(input())
number = list(map(int, value))
stack = [number[0]]

for i in range(1, N):
    while stack and stack[-1] < number[i] and K > 0:
        stack.pop()
        K -= 1
    stack.append(number[i])


for i in range(len(stack) - K):
    print(stack[i], end='')
