import sys

input = sys.stdin.readline
N = int(input())
arr = [0 for i in range(10001)]
for i in range(N):
    arr[int(input())] += 1
for i in range(10001):
    for j in range(arr[i]):
        print(i)

# def counting_sort(array, num):
#     cnt_arr = [0 for _ in range(num + 1)]
#     for i in array:
#         cnt_arr[i] += 1
#
#     for i in range(num):
#         cnt_arr[i + 1] += cnt_arr[i]
#
#     output_arr = [-1 for _ in range(N)]
#
#     for i in array:
#         output_arr[cnt_arr[i] - 1] = i
#         cnt_arr[i] -= 1
#
#     return output_arr
#
#
# ret = counting_sort(arr, max(arr))
#
# for i in ret:
#     sys.stdout.write(str(i))
#     sys.stdout.write('\n')
