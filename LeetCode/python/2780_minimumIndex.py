from collections import Counter
from typing import List


class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        size = len(nums)        
        dominant = Counter(nums).most_common(1)[0]        
    
    
        if dominant[1]*2 <= size:
            return -1
        if dominant[1] <= size//2+1 and size %2 != 0:
            return -1

        idx = 0
        for i, n in enumerate(nums):
            if n == dominant[0]:
                idx += 1
            if idx*2 > i+1:
                return i

        return -1

print(Solution().minimumIndex([1,2,2,2]))
print(Solution().minimumIndex([2,1,3,1,1,1,7,1,2,1]))
print(Solution().minimumIndex([3,3,3,3,7,2,2]))
        