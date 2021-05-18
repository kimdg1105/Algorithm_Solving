import sys
input = sys.stdin.readline

N, M = map(int,input().split())
trees = list(map(int,input().split()))

def bin_search(arr, target):
    start = max(arr)
    end = 0

    while start > end:

        mid = (start + end) // 2
        total = 0
        for i in range(len(arr)):
            if arr[i]-mid >= 0:
                total += arr[i]-mid
        if total > target:
            end = mid
        elif total < target:
            start = mid
        else:
            return mid
        #print("st, e", start, end)
        if abs(start-end) == 1:
            return end





print(bin_search(trees,M))