from typing import List


class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        ans = []
        a = 1

        for a in range(1, n):
            b = n - a
            if "0" not in str(a) + str(b):
                return [a, b]

        return ans


print(Solution().getNoZeroIntegers(2))
print(Solution().getNoZeroIntegers(11))
print(Solution().getNoZeroIntegers(4509))
