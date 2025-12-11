from itertools import combinations


def solution(n, q, ans):
    answer = 0
    combi = list(combinations([x for x in range(1, n + 1)], 5))

    for candidate in combi:
        for idx, test in enumerate(q):
            if len(set(test) & set(candidate)) != ans[idx]:
                break
            if idx == len(q) - 1:
                answer += 1

    return answer


# result: 3
print(
    solution(
        10,
        [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [3, 7, 8, 9, 10],
            [2, 5, 7, 9, 10],
            [3, 4, 5, 6, 7],
        ],
        [2, 3, 4, 3, 3],
    )
)

# result: 5
# print(
#     solution(
#         15,
#         [
#             [2, 3, 9, 12, 13],
#             [1, 4, 6, 7, 9],
#             [1, 2, 8, 10, 12],
#             [6, 7, 11, 13, 15],
#             [1, 4, 10, 11, 14],
#         ],
#         [2, 1, 3, 0, 1],
#     )
# )
