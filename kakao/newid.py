def solution(new_id):
    answer = ''

    lv1 = new_id.lower()
    # print(lv1)

    lv2 = ''
    for ch in lv1:
        if ch.isalnum() or ch in '-_.':
            lv2 += ch
    # print("lv2",lv2)

    lv3 = lv2
    while '..' in lv3:
        lv3 = lv3.replace('..', '.')
    # print("lv3",lv3)

    lv4 = lv3
    if len(lv4) > 1:
        if lv4[0] == '.':
            lv4 = lv4[1:]
        if lv4[-1] == '.':
            lv4 = lv4[:-1]
    else:
        if lv4 == '.':
            lv4 = ''
    # print('lv4',lv4)

    lv5 = lv4
    if lv5 == '':
        lv5 = 'a'
    # print('lv5',lv5)

    lv6 = lv5
    if len(lv6) >= 16:
        lv6 = lv6[:15]
        if lv6[-1] == ".":
            lv6 = lv6[:-1]

    # print('lv6',lv6)

    lv7 = lv6
    if len(lv7) <= 2:
        while len(lv7) != 3:
            lv7 += lv7[-1]

    # print('lv7',lv7)

    answer = lv7

    return answer