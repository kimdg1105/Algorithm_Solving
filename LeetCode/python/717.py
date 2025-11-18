from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        allow = ["10", "11"]
        except_last = bits[:-1]

        if len(except_last) == 0:
            return True

        cnt = 0
        for val in except_last:
            if val == 0:
                cnt += 1
            else:
                break
        if cnt == len(except_last):
            return True

        ans = False

        candidate = "".join(map(str, except_last))

        print(candidate)
        for val in allow:
            if val == candidate:
                ans = True

        return ans


print(Solution().isOneBitCharacter([0, 0]))
print(Solution().isOneBitCharacter([1, 0, 0]))
print(Solution().isOneBitCharacter([1, 1, 0, 0]))
