import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
tang = list(map(int, input().split()))


def solve_sliding_window():
    left = 0
    max_length = 0
    fruit_count = defaultdict(int)

    for right in range(n):
        fruit_count[tang[right]] += 1

        while len(fruit_count) > 2:
            fruit_count[tang[left]] -= 1
            if fruit_count[tang[left]] == 0:
                del fruit_count[tang[left]]
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length


print(solve_sliding_window())
