from collections import deque


def solution(prices):
    answer = []
    q = deque(prices)

    while q:
        sec = 0
        value = q.popleft()
        for price in q:
            sec += 1
            if value > price:
                break
        answer.append(sec)

    return answer


print(solution([1, 2, 3, 2, 3]))
