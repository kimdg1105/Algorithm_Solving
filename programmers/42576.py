def solution(participant, completion):
    answer = ""
    dict = {}

    for c in completion:
        if c not in dict:
            dict[c] = 1
        else:
            dict[c] += 1

    for p in participant:
        if p not in dict or dict[p] == 0:
            answer = p
            break

        if dict[p] > 0:
            dict[p] -= 1

    return answer


print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))

# print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))
