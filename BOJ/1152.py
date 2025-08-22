input = input()
input = input.strip()
arr = input.split(" ")
ans = 0
for val in arr:
    if val != "":
        ans += 1


print(ans)
