import heapq
from math import inf

N = int(input())
M = int(input())

s = [[] for i in range(N+1)]

for _ in range(M):
    a, b, c = map(int,input().split())
    s[a].append([b,c])

qs, qe = map(int,input().split())


def Dijkstra(start):
    heap = []
    dist = [inf] * (N + 1)
    dist[start] = 0

    heapq.heappush(heap, (0, start))

    while heap:
        cost, cur_node = heapq.heappop(heap)
        for next_node, c in s[cur_node]:
            if dist[next_node] > cost + c:
                dist[next_node] = cost + c
                heapq.heappush(heap,(dist[next_node], next_node))

    return dist

mydist = Dijkstra(qs)
print(mydist[qe])

