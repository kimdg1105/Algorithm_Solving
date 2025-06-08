def solution(A, B):
    answer = 0

    A.sort()
    B.sort()

    n = len(A)

    for i in range(n):
        answer += A[i] * B[-1 - i]

    return answer


print(solution([1, 2], [3, 4]))
