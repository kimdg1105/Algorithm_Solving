from heapq import heapify, heappop, heappush


def solution(scoville, K):
    answer = 0

    heapify(scoville)

    while True:
        first = heappop(scoville)

        if first >= K:
            break
        elif len(scoville) > 0:
            second = heappop(scoville)
            mix = first + (second * 2)
            heappush(scoville, mix)
            answer += 1
        else:
            return -1

    return answer


print(solution([1, 2, 3, 9, 10, 12], 7))  # 2
