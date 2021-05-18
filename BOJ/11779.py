import heapq
import copy
from sys import maxsize

N = int(input())
M = int(input())

s = [[] for _ in range(N+1)]
path = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int,input().split())
    s[a].append([b,c])
    #s[b].append([a,c])

qs, qe = map(int,input().split())


def Dijkstra(start):
    heap = []
    inf = maxsize
    dist = [inf] * (N + 1)

    if start in s[start][0]:
        dist[start] = s[start][0][1]
    else:
        dist[start] = 0

    heapq.heappush(heap, (start,0))

    while heap:
        cur_node, cur_cost = heapq.heappop(heap)

        if dist[cur_node] < cur_cost:
            continue

        path[cur_node].append(cur_node)

        for next_node, next_cost in s[cur_node]:
            if dist[next_node] > next_cost + cur_cost:
                dist[next_node] = next_cost + cur_cost
                heapq.heappush(heap, (next_node,dist[next_node]))
                path[next_node] = copy.deepcopy(path[cur_node])
    return dist, path


mydist, mypath = Dijkstra(qs)

# print(mydist)
# print(mypath)
print(mydist[qe])
print(len(mypath[qe]))
print(*mypath[qe])

