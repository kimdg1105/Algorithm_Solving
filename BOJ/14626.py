isbn = input()
arr = []
ans = -1
x = 0
for idx, val in enumerate(isbn):
    if val == "*":
        if idx % 2 == 0:
            x = 1
        else:
            x = 3
    else:
        if idx % 2 == 0:
            arr.append(int(val))
        else:
            arr.append(3 * int(val))


for i in range(10):
    if (sum(arr) + (x * i)) % 10 == 0:
        ans = i
        break

print(ans)
