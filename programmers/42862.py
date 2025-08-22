def solution(n, lost, reserve):
    answer = 0

    lost.sort()
    reserve.sort()

    for l in lost[:]:
        if l in reserve:
            reserve.remove(l)
            lost.remove(l)

    for l in lost[:]:
        if l - 1 in reserve[:]:
            reserve.remove(l - 1)
            lost.remove(l)
            continue
        elif l + 1 in reserve[:]:
            reserve.remove(l + 1)
            lost.remove(l)
            continue

    return n - len(lost)


print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))
# 5	[2, 4]	[1, 3, 5]	5
# 5	[2, 4]	[3]	4
# 3	[3]	[1]	2
