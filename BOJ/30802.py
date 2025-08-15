n = input()

arr = map(int, input().split())
t, p = map(int, input().split())

arr_ans = []
for size in arr:
    if size == 0:
        arr_ans.append(0)
        continue
    ans = 1
    bulk_t = size // t
    if size % t != 0:
        bulk_t += 1
    arr_ans.append(bulk_t)

bult_p = int(n) // p
remain = int(n) % p

print(sum(arr_ans))
print(bult_p, remain)
