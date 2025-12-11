def solution(storage, requests):
    answer = 0
    storage = [list(row) for row in storage]

    for req in requests:
        if len(req) == 1:
            cnt, storage = remove_g(storage, req)
            answer += cnt

        if len(req) == 2 and req[0] == req[1]:
            cnt, storage = remove_all(storage, req[0])
            answer += cnt

    return (len(storage) * len(storage[0])) - answer


def remove_g(storage, char):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    visited = [[False] * len(storage[0]) for _ in range(len(storage))]
    temp_set = set()

    q = []
    for i in range(len(storage)):
        for j in range(len(storage[i])):
            if i == 0 or i == len(storage) - 1 or j == 0 or j == len(storage[i]) - 1:
                if storage[i][j] == char:
                    temp_set.add((i, j))

                    continue

                if storage[i][j] == None:
                    q.append((i, j))

    while q:
        x, y = q.pop()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if (
                    0 <= nx < len(storage)
                    and 0 <= ny < len(storage[0])
                    and not visited[nx][ny]
            ):
                visited[nx][ny] = True
                if storage[nx][ny] == char:
                    temp_set.add((nx, ny))
                elif storage[nx][ny] is None:
                    q.append((nx, ny))

    for (
            x,
            y,
    ) in temp_set:
        storage[x][y] = None

    return len(temp_set), storage


def remove_all(storage, char):
    cnt = 0
    for i in range(len(storage)):
        for j in range(len(storage[i])):
            if storage[i][j] == char:
                cnt += 1
                storage[i][j] = None
    return cnt, storage


# 11
# print(solution(["AZWQY", "CAABX", "BBDDA", "ACACA"], ["A", "BB", "A"]))

# 4
print(solution(["HAH", "HBH", "HHH", "HAH", "HBH"], ["C", "B", "B", "B", "B", "H"]))

# 15
# print(solution(["CCCCC", "CABAC", "CABAC", "CCABC"], ["BB", "A"]))
