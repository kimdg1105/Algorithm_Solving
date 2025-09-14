n, m = map(int, input().split())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))


def check1(x, y):
    d1 = [(x, y), (x, y + 1), (x, y + 2), (x, y + 3)]
    d2 = [(x, y), (x, y - 1), (x, y - 2), (x, y - 3)]
    d3 = [(x, y), (x + 1, y), (x + 2, y), (x + 3, y)]
    d4 = [(x, y), (x - 1, y), (x - 2, y), (x - 3, y)]
    check_list = [d1, d2, d3, d4]

    ans = 0
    for list in check_list:
        cur_ans = 0
        for i, j in list:
            if 0 <= i < n and 0 <= j < m:
                cur_ans += arr[i][j]
        ans = max(ans, cur_ans)

    return ans


def check2(x, y):
    d1 = [(x, y), (x, y + 1), (x + 1, y), (x + 1, y + 1)]
    d2 = [(x, y), (x, y - 1), (x + 1, y - 1), (x + 1, y)]
    d3 = [(x, y), (x, y - 1), (x - 1, y - 1), (x - 1, y)]
    d4 = [(x, y), (x, y + 1), (x - 1, y), (x - 1, y + 1)]
    check_list = [d1, d2, d3, d4]

    ans = 0
    for list in check_list:
        cur_ans = 0
        for i, j in list:
            if 0 <= i < n and 0 <= j < m:
                cur_ans += arr[i][j]
        ans = max(ans, cur_ans)

    return ans


def check3(x, y):
    d1 = [(x, y), (x, y - 1), (x - 1, y - 1), (x - 2, y - 1)]
    d2 = [(x, y), (x - 1, y), (x - 1, y + 1), (x - 1, y + 2)]
    d3 = [(x, y), (x, y + 1), (x + 1, y + 1), (x + 2, y + 1)]
    d4 = [(x, y), (x + 1, y), (x + 1, y - 1), (x + 1, y - 2)]
    d5 = [(x, y), (x, y + 1), (x - 1, y + 1), (x - 2, y + 1)]
    d6 = [(x, y), (x + 1, y), (x + 1, y + 1), (x + 1, y + 2)]
    d7 = [(x, y), (x, y - 1), (x + 1, y - 1), (x + 2, y - 1)]
    d8 = [(x, y), (x - 1, y - 2), (x - 1, y - 1), (x - 1, y)]
    check_list = [d1, d2, d3, d4, d5, d6, d7, d8]

    ans = 0
    for list in check_list:
        cur_ans = 0
        for i, j in list:
            if 0 <= i < n and 0 <= j < m:
                cur_ans += arr[i][j]
        ans = max(ans, cur_ans)

    return ans


def check4(x, y):
    d1 = [(x, y), (x + 1, y), (x, y + 1), (x - 1, y + 1)]
    d2 = [(x, y), (x, y - 1), (x + 1, y), (x + 1, y + 1)]
    d3 = [(x, y), (x - 1, y), (x, y - 1), (x + 1, y - 1)]
    d4 = [(x, y), (x - 1, y - 1), (x - 1, y), (x, y + 1)]
    d5 = [(x, y), (x - 1, y), (x, y + 1), (x + 1, y + 1)]
    d6 = [(x, y), (x, y + 1), (x + 1, y), (x + 1, y - 1)]
    d7 = [(x, y), (x - 1, y - 1), (x, y - 1), (x + 1, y)]
    d8 = [(x, y), (x - 1, y), (x - 1, y + 1), (x, y - 1)]
    check_list = [d1, d2, d3, d4, d5, d6, d7, d8]

    ans = 0
    for list in check_list:
        cur_ans = 0
        for i, j in list:
            if 0 <= i < n and 0 <= j < m:
                cur_ans += arr[i][j]
        ans = max(ans, cur_ans)

    return ans


def check5(x, y):
    d1 = [(x, y), (x - 1, y), (x, y - 1), (x, y + 1)]
    d2 = [(x, y), (x - 1, y), (x, y + 1), (x + 1, y)]
    d3 = [(x, y), (x, y - 1), (x + 1, y), (x, y + 1)]
    d4 = [(x, y), (x, y - 1), (x + 1, y), (x - 1, y)]
    check_list = [d1, d2, d3, d4]

    ans = 0
    for list in check_list:
        cur_ans = 0
        for i, j in list:
            if 0 <= i < n and 0 <= j < m:
                cur_ans += arr[i][j]
        ans = max(ans, cur_ans)

    return ans


total_max = 0
for i in range(n):
    for j in range(m):
        total_max = max(total_max, check1(i, j))
        total_max = max(total_max, check2(i, j))
        total_max = max(total_max, check3(i, j))
        total_max = max(total_max, check4(i, j))
        total_max = max(total_max, check5(i, j))


print(total_max)
