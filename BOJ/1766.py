# 위상정렬
import heapq

N,M = map(int,input().split())
adj_list = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int,input().split())
    adj_list[a].append(b)


def topological_sort(adj):
    ans = []
    q = []
    indegree = [0 for _ in range(N+1)]

    for i in range(1,N+1):
        for j in adj[i]:
            indegree[j] += 1

    # print(indegree)

    for i in range(1,len(indegree)):
        if indegree[i] == 0:
           heapq.heappush(q,i)
    # print("Curr Stack",q)

    while q:
        node = heapq.heappop(q)
        ans.append(node)

        for i in adj_list[node]:
            indegree[i] -= 1
            if indegree[i] == 0:
                heapq.heappush(q, i)

    return ans


ret = topological_sort(adj_list)

print(*ret, sep=" ")





