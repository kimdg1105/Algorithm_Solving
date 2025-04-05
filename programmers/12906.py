def solution(arr):
    answer = []

    for idx, num in enumerate(arr):
        if len(answer) > 0:
            if answer[-1] == num:
                continue
        answer.append(num)

    return answer


print(solution([1, 1, 3, 3, 0, 1, 1]))
