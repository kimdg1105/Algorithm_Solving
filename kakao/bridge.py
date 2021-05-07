

stone = list(map(int,input().split()))
k = int(input())


def solution(stones, k):
    left, right = 1, max(stones)
    answer = 1
    while left <= right: #종료 조건
        mid = (left + right) // 2
        empty = 0
        flag = True
        for stone in stones:
            if stone < mid:
                empty += 1
                if empty == k:  # k개의 공백이 생기면 움직일 수 없다.
                    flag = False
                    break
            else:
                empty = 0
        if flag:  # 움직일 수 있는 값
            answer = max(answer, mid)
            left = mid + 1
        else:
            right = mid - 1
    return answer

solution(stone,k)


# case
# 2 4 5 3 2 1 4 2 5 1
# 3