def solution(numbers, target):
    answer = 0
    graph = [[] for _ in range(len(numbers))]

    graph[0].append(numbers[0])
    graph[0].append(-1 * numbers[0])

    for idx in range(1, len(numbers)):
        base = graph[idx - 1]
        for b in base:
            graph[idx].append(b + numbers[idx])
            graph[idx].append(b + -1 * numbers[idx])

    last = graph[len(numbers) - 1]

    for cand in last:
        if cand == target:
            answer += 1
    return answer


print(solution([1, 1, 1, 1, 1], 3))
print(solution([4, 1, 2, 1], 4))
