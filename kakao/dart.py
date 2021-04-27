import sys
import re

input = sys.stdin.readline


def solution(dartResult):
    p = re.compile('([0-9]+)([SDT])([#*]?)')

    carry = p.findall(dartResult)  ## 파싱완료
    bucket = []
    for i in range(len(carry)):
        topic = carry[i]
        point = 0

        if topic[1] == 'S':
            point += int(topic[0])
        elif topic[1] == 'D':
            point += pow(int(topic[0]), 2)
        elif topic[1] == 'T':
            point += pow(int(topic[0]), 3)

        if topic[2] == '*':
            if i > 0:
                bucket[i-1] *=2
            point = 2 * point
        elif topic[2] == '#':
            point = -1 * point
        bucket.append(point)


    answer = sum(bucket)

    return answer


res = input()

print(solution(res))
