from collections import defaultdict, deque


n, m = map(int, input().split())
party_dict = defaultdict()
person_dict = defaultdict()
ans_party = defaultdict()
visited = [False for _ in range(n + 1)]


truth = list(map(int, input().split()))

for i in range(1, n + 1):
    person_dict[i] = []

for i in range(1, m + 1):
    ans_party[i] = True

    persons = list(map(int, input().split()))[1:]
    party_dict[i] = persons

    for person in persons:
        person_dict[person].append(i)


q = deque(truth[1:])

while q:
    now_person = q.popleft()
    visited[now_person] = True
    persons_party = person_dict[now_person] if person_dict[now_person] else []
    for lie_party in persons_party:
        ans_party[lie_party] = False
        for person in party_dict[lie_party]:
            if not visited[person]:
                q.append(person)


cnt = 0
for node in ans_party:
    if ans_party[node]:
        cnt += 1

print(cnt)
