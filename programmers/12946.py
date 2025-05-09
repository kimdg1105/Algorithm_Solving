def solution(n):
    answer = []
    hanoi(n, 1, 3, 2, answer)
    return answer


def hanoi(plate, start, end, via, ans):
    if plate == 1:
        move(plate, start, end, ans)
        return ans

    hanoi(plate - 1, start, via, end, ans)
    move(plate, start, end, ans)
    hanoi(plate - 1, via, end, start, ans)


def move(plate, start, end, ans):
    ans.append([start, end])
    return ans


print(solution(2))
