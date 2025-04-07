def solution(nums):
    answer = 0
    dict = {}
    for num in nums:
        if num not in dict:
            dict[num] = 0
        dict[num] += 1

    pick = len(nums) // 2

    return min(pick, len(dict))


print(solution([3, 3, 3, 2, 2, 4]))
