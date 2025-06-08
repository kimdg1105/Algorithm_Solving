def solution(distance, rocks, n):
    answer = 0
    rocks.sort()

    def getDistance(threshold):
        dist = 0
        before = 0
        stone_cnt = 0

        for idx, rock in enumerate(rocks):
            dist = rock - before
            if dist < threshold:
                stone_cnt += 1
            else:
                before = rock

            if idx == len(rocks) - 1:
                if distance - before < threshold:
                    stone_cnt += 1

        return stone_cnt

    left, right = 0, distance
    while left <= right:
        mid = (left + right) // 2
        stone_remove = getDistance(mid)
        if stone_remove > n:
            right = mid - 1
        else:
            left = mid + 1
            answer = max(answer, mid)

    return answer


print(solution(25, [2, 14, 11, 21, 17], 2))
