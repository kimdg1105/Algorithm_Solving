def solution(N, number):
    memo = {}

    for i in range(1, 9):
        arr = set()
        if i == 1:
            arr.add(N)
        else:
            arr.add(int(str(N) * (i)))
            for j in range(1, i):
                for comb1 in memo[i - j]:
                    for comb2 in memo[j]:
                        new_v1 = comb1 + comb2
                        new_v2 = comb1 - comb2
                        new_v3 = comb1 * comb2
                        if comb2 != 0:
                            new_v4 = comb1 // comb2

                        arr.add(new_v1)
                        arr.add(new_v2)
                        arr.add(new_v3)
                        arr.add(new_v4)

        memo[i] = set(arr)

        if number in memo[i]:
            return i

    return -1


print(solution(1, 121))
