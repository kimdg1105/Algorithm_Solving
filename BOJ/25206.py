line = 20
up = 0
total_hak = 0
dict = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0,
}
for i in range(line):
    word = input().split(" ")

    if word[2] not in ["P"]:
        up += float(word[1]) * dict[word[2]]
        total_hak += float(word[1])


def my_round(f: float) -> int:
    res = int(abs(f) + 0.5)
    return res if f >= 0 else -res


print(up)
print(my_round(up / total_hak))
