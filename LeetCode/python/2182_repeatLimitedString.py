from heapq import heappop, heappush
from typing import Counter


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        counter = Counter(s)
        max_heap = []
        ans = []

        for c, cnt in counter.items():
            heappush(max_heap, (-ord(c), cnt))

        while max_heap:
            uni, cnt = heappop(max_heap)
            char = chr(-uni)

            use_cnt = min(cnt, repeatLimit)
            ans.extend([char] * use_cnt)
            cnt -= use_cnt

            if cnt > 0:
                if not max_heap:
                    break
                next_uni, next_cnt = heappop(max_heap)
                next_char = chr(-next_uni)

                ans.append(next_char)
                next_cnt -= 1

                if next_cnt > 0:
                    heappush(max_heap, (next_uni, next_cnt))
                heappush(max_heap, (uni, cnt))

        return "".join(ans)


sol = Solution()
# print(sol.repeatLimitedString("cczazcc", 3))
# print(sol.repeatLimitedString("aababab", 2))
# print(
#     sol.repeatLimitedString(
#         "gapqzytcgvbqnyucmvhzusqrebydzqnlyqjlglssdhjgiecnritocbfexnvnmrgcoayorbmexhazxtwshari",
#         9,
#     )
# )
print(
    sol.repeatLimitedString(
        "xyutfpopdynbadwtvmxiemmusevduloxwvpkjioizvanetecnuqbqqdtrwrkgt", 1
    )
)
