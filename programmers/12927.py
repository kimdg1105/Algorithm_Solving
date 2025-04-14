from heapq import heappop, heappush


def solution(n, works):
    answer = 0
    heap = []
    for work in works:
        heappush(heap, (-1 * work, work))

    while heap and n != 0:
        biggest = heappop(heap)
        if biggest[1] == 0:
            break
        do_work = biggest[1] - 1
        heappush(heap, (-1 * do_work, do_work))
        n -= 1

    new_works = [work[1] for work in heap]
    answer += calTired(new_works)
    return answer


def calTired(works):
    tired = 0
    for work in works:
        tired += work**2
    return tired


# print(solution(4, [4, 3, 3]))
print(solution(3, [1, 1]))
