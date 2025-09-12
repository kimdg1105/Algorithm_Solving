import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
s = input().strip()

count = 0
i = 0

while i < m:
    if s[i] == "I":
        ioi_count = 0
        j = i

        while j + 2 < m and s[j] == "I" and s[j + 1] == "O" and s[j + 2] == "I":
            ioi_count += 1
            j += 2

        if ioi_count >= n:
            count += ioi_count - n + 1

        i = max(i + 1, j)
    else:
        i += 1

print(count)
