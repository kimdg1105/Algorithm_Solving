import sys
import re
input = sys.stdin.readline


tu = input().strip()


def solution(s):
    answer = []
    s = s[2:-2]
    s = s.split("},{")

    num_list = []
    for i in s:
        num_list.append(i.split(","))

    #
    num_list.sort(key= lambda x: len(x))

    for i in num_list:
        for j in i:
            if not j in answer:
                answer.append(j)

    answer = list(map(int,answer))




    return answer

print(solution(tu))