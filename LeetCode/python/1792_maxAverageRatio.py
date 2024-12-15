from heapq import heappush, heappop
from typing import List

class Solution:
    def getNextRatio(self, a,b):
        return ((a+1)/(b+1)- a/b)

    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        max_heap = []
        
        for c in classes:
            heappush(max_heap, (-self.getNextRatio(c[0], c[1]), c[0], c[1]))
        
        while extraStudents != 0:
            diff, pass_cnt, total_cnt = heappop(max_heap)
            heappush(max_heap, (-self.getNextRatio(pass_cnt+1,total_cnt+1), pass_cnt+1,total_cnt+1))
            extraStudents -=1
            
        sum = 0
        for _, pa, total in max_heap:
            sum += pa / total
        return sum/len(classes)
    
sol = Solution()

print(sol.maxAverageRatio([[1,2],[3,5],[2,2]], 2))
print(sol.maxAverageRatio([[2,4],[3,9],[4,5],[2,10]], 4))

