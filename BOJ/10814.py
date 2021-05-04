N = int(input())
list = []
for i in range(N):
    age, name = input().split()
    list.append([age, name, i])
# for i in range(N):
#     for j in range(N):
#         if list[j][0] > list[i][0]:
#             temp = list[j][0]
#             list[j][0] = list[i][0]
#             list[i][0] = temp
list.sort(key=lambda x: (int(x[0]), int(x[2])))
for i in range(N):
    print(list[i][0], list[i][1])
