import math
from typing import List


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(k):
            gifts.sort()
            gifts[-1] = int(math.sqrt(gifts[-1]))

        return sum(gifts)


sol = Solution()
print(sol.pickGifts([25, 64, 9, 4, 100], 4))


# [25,64,9,4,100], k = 4
# [25,64,9,4,10] k=3
# [25,8,9,4,10] k=2
# [5,8,9,4,10] k=1
# [5,8,9,4,3] k =0
