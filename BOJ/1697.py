from collections import deque


n, k = map(int, input().split())


arr = [0 for _ in range(100001)]
visited = [False for _ in range(100001)]

q = deque()
q.append(n)
visited[n] = True


while q:
    val = q.popleft()
    if val == k:
        break
    for way in (val - 1, val + 1, 2 * val):
        if 0 <= way < 100001:
            if not visited[way]:
                q.append(way)
                arr[way] = arr[val] + 1
                visited[way] = True


print(arr[k])
