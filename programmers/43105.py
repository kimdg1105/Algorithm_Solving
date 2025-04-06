def solution(triangle):
    answer = 0
    dp = [[0] for _ in range(len(triangle))]

    for idx, line in enumerate(triangle):
        if idx == 0:
            dp[idx] = line
        else:
            arr = []
            for j, val in enumerate(line):
                if j == 0:
                    new_val = dp[idx - 1][j] + val
                elif j == len(line) - 1:
                    new_val = dp[idx - 1][j - 1] + val
                else:
                    new_val = max(dp[idx - 1][j - 1] + val, dp[idx - 1][j] + val)
                arr.append(new_val)
            dp[idx] = arr

    return max(dp[len(triangle) - 1])


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
