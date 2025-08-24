def roundUp(num):
    if (num - int(num)) >= 0.5:
        return int(num) + 1
    else:
        return int(num)


n = int(input())
arr = []
ans = 0

for _ in range(n):
    arr.append(int(input()))

arr.sort()

exclude = roundUp(n * 0.15)

arr2 = arr[exclude : n - exclude]
if len(arr2) == 0:
    print(0)
else:
    print(round(sum(arr2) / len(arr2)))
