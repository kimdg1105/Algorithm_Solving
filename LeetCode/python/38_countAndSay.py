class Solution:
    def rle(self, nums: str) -> str:
        result = ""

        cur = None
        cur_cnt = 0
        for val in nums:
            if cur == None:
                cur = val
                cur_cnt += 1
            elif cur == val:
                cur_cnt += 1
            else:
                result += str(cur_cnt) + cur
                cur = val
                cur_cnt = 1
        if cur != None:
            result += str(cur_cnt) + cur
        return result

    def countAndSay(self, n: int) -> str:
        if n == 1:
            return str(1)
        else:
            return self.rle(self.countAndSay(n - 1))


print(Solution().countAndSay(4))
