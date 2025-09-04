n, m = map(int, input().split())

dnas = []
ans_dna = [{} for _ in range(m)]

for _ in range(n):
    dna = input()
    dnas.append(dna)
    for idx, char in enumerate(dna):
        if char not in ans_dna[idx]:
            ans_dna[idx][char] = 0
        else:
            ans_dna[idx][char] += 1


ans = ""
cnt = 0
for d in ans_dna:
    d2 = sorted(d.items(), key=lambda x: (-x[1], x[0]))
    top = d2[0][0]
    # p = len(d2) - 1
    # cnt += p
    ans += top


print(ans)


for dna in dnas:
    for idx, char in enumerate(dna):
        if char != ans[idx]:
            cnt += 1

print(cnt)
