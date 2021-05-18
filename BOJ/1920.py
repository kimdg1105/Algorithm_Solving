N = int(input())
n_list = list(map(int,input().split()))

M = int(input())
m_list = list(map(int,input().split()))

n_list.sort()

def bin_search(arr, target):
    start = 0
    end = len(arr)-1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return 1
        elif arr[mid] > target:
            end = mid-1
        elif arr[mid]  < target:
            start = mid+1
    return  0

for i in range(len(m_list)):
    print(bin_search(n_list, m_list[i]))