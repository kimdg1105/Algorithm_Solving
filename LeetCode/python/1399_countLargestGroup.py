from collections import defaultdict


class Solution:
    def countLargestGroup(self, n: int) -> int:
        cnt = 0
        ans = 0
        dict = defaultdict(list)
        for i in range(1, n + 1):
            if i < 10:
                dict[i] = [i]
            else:
                str_i = list(map(int, str(i)))
                sum_i = sum(str_i)

                dict[sum_i].append(i)

        for k in dict.keys():
            cnt = max(cnt, len(dict[k]))

        for k in dict.keys():
            if len(dict[k]) == cnt:
                ans += 1

        return ans


print(Solution().countLargestGroup(13))
