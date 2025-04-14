from typing import List


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        answer = 0
        for i in range(len(arr) - 2):
            ai = arr[i]
            for j in range(i + 1, len(arr) - 1):
                aj = arr[j]
                if abs(ai - aj) > a:
                    continue
                for k in range(j + 1, len(arr)):
                    ak = arr[k]
                    jk = abs(aj - ak)
                    if jk > b:
                        continue
                    if abs(ai - ak) <= c:
                        answer += 1
        return answer


print(Solution().countGoodTriplets([3, 0, 1, 1, 9, 7], 7, 2, 3))
