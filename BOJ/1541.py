input = input()

num_arr = input.split("-")

first_neg = 1
if input[0] == "-":
    first_neg = -1

ans = []

for num_str in num_arr:
    num_sub_arr = map(int, num_str.split("+"))
    ans.append(sum(num_sub_arr))

ans[0] = first_neg * ans[0]

total = ans[0]

for a in ans[1:]:
    total += -a

print(total)
