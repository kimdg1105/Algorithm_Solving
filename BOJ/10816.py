# N = int(input())
# card = list(map(int,input().split()))
# M = int(input())
# tofind = []
# tofind = list(map(int,input().split()))
#
# card.sort()
#
# def bin_search(arr,target):
#     start = 0
#     end = len(arr)-1
#
#     while start <= end:
#         mid = (start + end) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] > target:
#             end = mid-1
#         else:
#             start = mid+1
#     return -1
#
# def check_left(arr, idx, target):
#     cnt = 0
#     while True:
#         if idx < 0 or arr[idx] != target:
#             break
#         cnt += 1
#         idx -= 1
#     return cnt
#
# def check_right(arr, idx, target):
#     cnt = 0
#     while True:
#         if idx > len(arr)-1 or arr[idx] != target:
#             break
#         cnt += 1
#         idx += 1
#     return cnt
#
# ret = []
#
# for i in range(len(tofind)):
#     idx = bin_search(card, tofind[i])
#
#     if idx != -1:
#         total = 1
#         total += check_left(card, idx - 1, tofind[i])
#         total += check_right(card, idx + 1, tofind[i])
#         ret.append(total)
#     else:
#         ret.append(0)
#
#
# for r in ret:
#     print(r, end=" ")


N = int(input())
card = list(map(int,input().split()))
M = int(input())
tofind = []
tofind = list(map(int,input().split()))

mydict = {}

for c in card:
    if c not in mydict:
        mydict[c] = 1
    else:
        mydict[c] += 1

for tf in tofind:
    if tf in mydict:
        print(mydict[tf], end =" ")
    else:
        print(0, end=" ")