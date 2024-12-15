from collections import deque
from typing import List

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        start = 0
        ans = 0
        min_deque = deque()
        max_deque = deque()
        
        for end in range(len(nums)):
            while min_deque and nums[min_deque[-1]] >= nums[end]:
                min_deque.pop()
            min_deque.append(end)
            
            while max_deque and nums[max_deque[-1]] <= nums[end]:
                max_deque.pop()
            max_deque.append(end)
            
            while min_deque and max_deque and  nums[max_deque[0]] - nums[min_deque[0]] > 2:
                start += 1
                if min_deque[0] < start:
                    min_deque.popleft()
                if max_deque[0] < start:
                    max_deque.popleft()
            
            ans += end - start + 1       
        return ans
    

sol = Solution()
print(sol.continuousSubarrays([5,4,2,4]))
print(sol.continuousSubarrays([1,2,3]))
print(sol.continuousSubarrays([65,66,67,66,66,65,64,65,65,64]))



