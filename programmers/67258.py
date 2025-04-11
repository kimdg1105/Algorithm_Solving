def solution(gems):
    all_gems = set(gems)
    answer = [1, len(gems)]
    dict = {}

    start, end = 0, 0

    while end < len(gems):
        if gems[end] not in dict:
            dict[gems[end]] = 1
        else:
            dict[gems[end]] += 1

        while len(dict) == len(all_gems):
            if len(answer) == 2 and end - start < answer[1] - answer[0]:
                answer[0], answer[1] = start + 1, end + 1

            dict[gems[start]] -= 1
            if dict[gems[start]] == 0:
                del dict[gems[start]]
            start += 1

        end += 1

    return answer


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
print(solution(["A", "B", "B", "C", "A", "C", "B", "B", "A"]))
