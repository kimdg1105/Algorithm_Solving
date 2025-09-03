import sys


input = sys.stdin.readline
blue, white = 0, 0

n = int(input())

matrix = [[] for _ in range(n)]
for i in range(n):
    matrix[i] = list(map(int, input().split()))


def divide(arr: list[list[int]]):
    n = len(arr)
    tobe_n = n // 2
    a, b, c, d = (
        [row[:tobe_n] for row in arr[:tobe_n]],
        [row[tobe_n:] for row in arr[:tobe_n]],
        [row[:tobe_n] for row in arr[tobe_n:]],
        [row[tobe_n:] for row in arr[tobe_n:]],
    )
    return [a, b, c, d]


def checkColor(arr: list[list[int]]):
    color = arr[0][0]

    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] != color:
                return False
    if color == 1:
        global white
        white += 1
    else:
        global blue
        blue += 1

    return True


todo = [matrix]
while todo:
    todo_check = todo.pop()
    if checkColor(todo_check):
        continue
    else:
        divided_arr = divide(todo_check)
        todo += divided_arr

print(blue)
print(white)
