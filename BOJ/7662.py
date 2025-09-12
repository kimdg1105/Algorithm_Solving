from heapq import heappop, heappush
import sys

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    min_heap = []
    max_heap = []

    k = int(input())
    visited = [False] * k
    for i in range(k):
        cal, num = input().split()
        if cal == "I":
            heappush(min_heap, (int(num), i))
            heappush(max_heap, (-int(num), i))
            visited[i] = True

        if cal == "D":
            if num == "1":
                while max_heap and not visited[max_heap[0][1]]:
                    heappop(min_heap)
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heappop(max_heap)

            elif num == "-1":
                while min_heap and not visited[min_heap[0][1]]:
                    heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = False
                    heappop(min_heap)
        while min_heap and not visited[min_heap[0][1]]:
            heappop(min_heap)
        while max_heap and not visited[max_heap[0][1]]:
            heappop(max_heap)

    print(-max_heap[0][0], min_heap[0][0]) if max_heap and min_heap else print("EMPTY")
