import datetime

def solution(lines):
    answer = 0
    total_stack = []
    st_stack, end_stack = [],[]
    i = 1
    for log in lines:
        log_split = log.split(" ")
        ymd = log_split[0]
        end = log_split[1]
        T = float(log_split[2][:-1])

        et = ''.join(ymd + 'T' + end)

        T = float(T)
        print("my T",T)
        # T_s = int(T//1)
        # T_ms = int(T%1)

        end_time = datetime.datetime.fromisoformat(et)
        T = datetime.timedelta(seconds=T)

        st_time = end_time - T + datetime.timedelta(seconds=0.001)
        st_stack.append((st_time))
        end_stack.append((end_time))

        i += 1

    total_stack = st_stack + end_stack
    search_sec = datetime.timedelta(seconds=1)
    mymax = 0

    for t in total_stack:
        res = 0
        for j in range(len(end_stack)):
            if t <= end_stack[j] < t + search_sec or t <= st_stack[j] < t + search_sec:
                res +=1
            elif st_stack[j] <= t and end_stack[j] >= t + search_sec:
                res +=1

        if mymax < res:
            mymax = res

    #print("max",mymax)
    return mymax

lines = list(map(str,input().split(",")))


solution(lines)