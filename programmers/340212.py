def solution(diffs, times, limit):
    low, high = 1, max(diffs)

    while low <= high:
        mid = (low + high) // 2
        result = doWithLv(diffs, times, limit, mid)
        if result == True:
            high = mid - 1
        else:
            low = mid + 1

    return low


def doWithLv(diffs, times, limit, level) -> bool:
    answer = times[0]
    for i in range(1, len(diffs)):
        answer += gameProcess(diffs[i], times[i], times[i - 1], level)
    if answer <= limit:
        return True
    return False


def gameProcess(diff, time_cur, time_prev, level):
    if diff <= level:
        return time_cur
    else:
        wrong_cnt = diff - level
        wrong_time = wrong_cnt * (time_prev + time_cur)
        return time_cur + wrong_time


print(solution([1, 5, 3], [2, 4, 7], 30))
print(solution([1, 99999, 100000, 99995], [9999, 9001, 9999, 9001], 3456789012))
