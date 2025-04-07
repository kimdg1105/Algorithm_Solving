def solution(answers):
    answer = []
    max_q = 10000

    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    dict = {1: 0, 2: 0, 3: 0}

    for idx, collect in enumerate(answers):
        if collect == one[idx % len(one)]:
            dict[1] += 1
        if collect == two[idx % len(two)]:
            dict[2] += 1
        if collect == three[idx % len(three)]:
            dict[3] += 1

    ans = max(dict.values())

    for k, v in dict.items():
        if v == ans:
            answer.append(k)

    return answer


print(solution([1, 2, 3, 4, 5]))
