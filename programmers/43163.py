from collections import defaultdict, deque


def solution(begin, target, words):
    words.append(begin)
    dict = defaultdict(list)
    target_idx = -1
    for i in range(len(words)):
        dict[i] = []

    for i in range(len(words)):
        for j in range(len(words)):
            if words[j] == target:
                target_idx = j
            if isConnected(words[i], words[j]):
                dict[i].append((j, words[j]))
    if target_idx == -1:
        return 0

    visited = {}
    q = deque()

    start, depth = len(words) - 1, 0
    q.append((start, begin, depth))

    while q:
        next = q.popleft()
        visited[next[0]] = True

        if next[0] == target_idx:
            return next[2]
        for candidate in dict[next[0]]:
            if candidate[0] not in visited:
                q.append((candidate[0], candidate[1], next[2] + 1))

    return 0


def isConnected(a, b):
    diff = 0
    idx = 0
    while idx != len(a) or idx != len(b):
        if a[idx] != b[idx]:
            diff += 1
        idx += 1

    if diff == 1:
        return True
    return False


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
print(solution("AAAA", "AABB", ["AABA", "AABB"]))
print(solution("aaa", "bbb", ["aab", "abb", "bbb"]))
print(solution("hit", "cog", ["cog", "log", "lot", "dog", "dot", "hot"]))
