def solution(schedules, timelogs, startday):
    answer = 0
    ans = [True for _ in range(len(schedules))]

    for idx, schedule in enumerate(schedules):
        day = startday
        if ans[idx] == False:
            continue

        end_time = make_end_time(schedule)
        for timelog in timelogs[idx]:
            if day == 6 or day == 7:
                continue
            if timelog > end_time:
                ans[idx] = False
                continue
            if day < 7:
                day += 1
            else:
                day = 1

    for a in ans:
        if a == True:
            answer += 1

    return answer


def make_end_time(timelog):
    end_time = timelog + 10
    hour = end_time // 100
    minute = end_time % 100

    if minute >= 60:
        minute = minute - 60
        hour += 1

    return hour * 100 + minute


print(
    solution(
        [700, 800, 1100],
        [
            [710, 2359, 1050, 700, 650, 631, 659],
            [800, 801, 805, 800, 759, 810, 809],
            [1105, 1001, 1002, 600, 1059, 1001, 1100],
        ],
        5,
    )
)

print(
    solution(
        [730, 855, 700, 720],
        [
            [710, 700, 650, 735, 700, 931, 912],
            [908, 901, 805, 815, 800, 831, 835],
            [705, 701, 702, 705, 710, 710, 711],
            [707, 731, 859, 913, 934, 931, 905],
        ],
        1,
    )
)
