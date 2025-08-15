x = int(input())
n = int(input())

total = 0

for _ in range(n):
    list = input()
    price, count = list.split(" ")
    price_item = int(price) * int(count)
    total += price_item

print("Yes" if total == x else "No")
