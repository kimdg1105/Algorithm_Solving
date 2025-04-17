def solution(n, times):
    answer = 0

    max_time = max(times) * n
    start, end = 0, max_time

    while start <= end:
        mid = (start + end) // 2
        pass_cnt = 0
        for time in times:
            pass_cnt += mid // time

            if pass_cnt >= n:
                break

        if pass_cnt >= n:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
    return answer


# print(solution(6, [7, 10]))
print(solution(6, [2, 5]))  # 10
