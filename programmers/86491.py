def solution(sizes):
    answer = 0
    w, h = [], []

    for i in range(0, len(sizes)):
        w.append(max(sizes[i]))
        h.append(min(sizes[i]))

    return max(w) * max(h)


print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
