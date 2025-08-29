n = int(input())
edge = int(input())

dict = dict()
for i in range(1, n + 1):
    dict[i] = []

for _ in range(edge):
    a, b = map(int, input().split())
    dict[a].append(b)
    dict[b].append(a)

virus = [1]
visited = []
queue = [1]


while queue:
    element = queue.pop()
    for node in dict[element]:
        if node not in visited:
            if node != 1:
                visited.append(node)
            queue.append(node)


print(dict)
print(visited)
print(len(visited))
