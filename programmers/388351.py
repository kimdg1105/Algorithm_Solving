def solution(schedules, timelogs, startday):
    answer = 0
    due_time = []
    for s in schedules:
        s += 10
        if s % 100 >= 60:
            s += 40
        due_time.append(s)

    for idx, person in enumerate(timelogs):
        cur_day = startday
        gift = True
        for day in person:
            if cur_day == 8:
                cur_day = 1
            if cur_day in [6, 7]:
                cur_day += 1
                continue
            if due_time[idx] < day:
                gift = False
                break
            cur_day += 1
        if gift:
            answer += 1

    return answer


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
