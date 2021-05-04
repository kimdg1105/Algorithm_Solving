import sys

input = sys.stdin.readline

N = int(input())

board = []

for _ in range(N):
    board.append(list(map(int, input().split())))

move = list(map(int, input().split()))


def check(stack) -> int:
    length = len(stack)
    if length >= 2:
        if stack[-1] == stack[-2]:
            #print("cnt up with,",stack)
            stack.pop()
            stack.pop()

            return 2
    else:
        return 0
    return 0


def solution(board, moves):
    answer = 0
    stack = []
    for m in moves:
        line = 0
        while line < len(board):
            # if line == N:
            #     break
            if board[line][m - 1] != 0:
                stack.append(board[line][m - 1])
                #print("current stack:",stack)
                board[line][m - 1] = 0
                pop_cnt = check(stack)
                answer += pop_cnt
                # for k in board:
                #     print(k)
                break


            else:
                line += 1



    return answer


print(solution(board, move))
