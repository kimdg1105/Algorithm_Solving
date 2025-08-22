def solution(n, w, num):
    arr = {}
    box = 1
    horizen = 0
    reverse = False
    for x in range(n):
        x_index = 0
        if box % w == 0:
            horizen += 1
        arr[box] = (horizen, x)
        box += 1

    print(arr)
    return 1


solution(22, 6, 8)
