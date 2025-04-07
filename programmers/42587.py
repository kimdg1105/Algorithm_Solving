def solution(priorities, location):
    answer = 0
    result = []
    q = []

    for idx, p in enumerate(priorities):
        q.append((idx, p))

    while q:
        cur_p = q.pop(0)
        if not q:
            result.append(cur_p[0])
            break

        cur_max = max(q, key=lambda x: x[1])

        if cur_max[1] > cur_p[1]:
            q.append(cur_p)
        else:
            result.append(cur_p[0])

    print(result)

    return result.index(location) + 1


print(solution([2, 1, 3, 2], 2))
