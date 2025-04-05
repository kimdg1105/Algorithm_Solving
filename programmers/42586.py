import heapq


def solution(progresses, speeds):
    answer = []
    date_q = []

    for progress, speed in zip(progresses, speeds):
        date_q.append(checkDueDate(progress, speed))

    day = 0
    while date_q:
        work_cnt = 0
        cur_work = date_q[0]
        while day < cur_work:
            day += 1

        while day >= cur_work:
            work_cnt += 1
            date_q.pop(0)
            if not date_q:
                break
            cur_work = date_q[0]
        answer.append(work_cnt)

    return answer


def checkDueDate(progress, speed):
    remain = 100 - progress
    day_work = remain // speed
    if remain % speed != 0:
        day_work += 1
    return day_work


print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
