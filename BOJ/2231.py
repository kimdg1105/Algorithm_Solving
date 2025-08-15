n = input()
max = 1_000_000
ans = 0
for i in range(1, max + 1):
    base = i
    char_base = str(base)
    for char in char_base:
        base += int(char)

    if int(n) == base:
        ans = i
        break

print(ans)
