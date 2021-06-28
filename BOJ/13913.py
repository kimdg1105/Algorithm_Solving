from collections import deque
N,K = map(int,input().split())

pp = {}
visited = [False for _ in range(100001)]

def findPath(k):
    arr = []
    now = k
    arr.append(now)
    while pp[now] != N:
        arr.append(pp[now])
        now = pp[now]
    arr.append(pp[now])
    arr.reverse()
    return arr


def bfs(n, cnt):
    dq = deque()
    dq.append([n, cnt])
    visited[n] = True

    while dq:
        nx, ncnt = dq.popleft()
        visited[nx] = True
        if nx == K:
            return ncnt

        for next in (nx+1,nx-1,nx*2):
            if 0 <= next <= 100000 and not visited[next]:
                visited[next] = True
                pp[next] = nx
                dq.append([next,ncnt+1])
        # if 0 <= nx + 1 <= 100000 and not visited[nx+1]:
        #     dq.append([nx+1,ncnt+1])
        #     visited[nx+1] = True
        #     path[nx+1] = nx
        # if 0 <= nx - 1 <= 100000 and not visited[nx-1]:
        #     dq.append([nx-1,ncnt+1])
        #     visited[nx-1] = True
        #     path[nx - 1] = nx
        # if 0 <= nx * 2 <=100000 and not visited[nx *2]:
        #     dq.append([nx *2,ncnt+1])
        #     visited[nx*2] = True
        #     path[nx*2] = nx




ret_cnt = bfs(N, 0)
if N != K:
    ret_path = findPath(K)
    print(ret_cnt)
    print(*ret_path, sep=' ')
else:
    ret_path = N
    print(ret_cnt)
    print(ret_path)





