def solution(board):
    answer = 0
    N = len(board)
    start_x, stary_y = -1, -1
    trace = {(start_x, stary_y): [False, False, False, False]}
    count = 0

    for i in range(N):
        for j in range(N):
            if board[i][j] == "G":
                start_x, stary_y = i, j

    def dfs(x, y, trace):
        dx = [1, 0, 0, -1]
        dy = [0, -1, 1, 0]

        for i in range(len(dx)):
            nx, ny = x + dx, y + dy
            if (nx, ny) in trace and trace[(nx, ny)][i] == False:
                trace[(nx, ny)][i] = True
                count += 1
                if board[nx, ny] == "D" or nx > N or ny < N:
                    dfs(nx, ny, trace)

    dfs(start_x, stary_y, trace)

    return answer


print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))
