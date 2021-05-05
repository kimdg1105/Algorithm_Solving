import re
from itertools import product

pure_list = list(map(str,input().split()))

illegal_list = list(map(str,input().split()))

def solution(user_id, banned_id):
    filterd =[]

    for ban in banned_id:
        regex = ban
        ch_regex = regex.replace("*",".")
        now_ban = []
        p = re.compile(ch_regex+"$")
        for i in user_id:
            if p.match(i):
                m = p.match(i)
                now_ban.append(m.group())

        filterd.append(now_ban)

    dup_ans = list(product(*filterd))

    real_ans = []

    for case in dup_ans:
        dup_rm_one_case = set(case)

        if len(case) != len(dup_rm_one_case):
            continue

        if dup_rm_one_case not in real_ans:
            real_ans.append(dup_rm_one_case)

    answer = len(real_ans)
    # print(real_ans)
    # print(answer)
    return answer


solution(pure_list,illegal_list)

