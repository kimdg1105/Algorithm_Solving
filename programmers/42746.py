def solution(numbers):
    arr = []
    answer = ""

    numbers = sort_by_largest_digit(numbers)
    print(numbers)

    answer = answer.join(map(str, numbers))

    return str(int(answer))


def sort_by_largest_digit(numbers):
    return sorted(numbers, key=lambda x: (max(map(int, str(x))), x), reverse=True)


print(solution([6, 10, 2]))
print(solution([10, 11, 12, 13]))
