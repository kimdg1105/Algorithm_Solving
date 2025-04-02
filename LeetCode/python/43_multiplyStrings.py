class Solution:
    def getNumeric(self, num: str) -> int:
        result = 0
        length = len(num)
        for idx, val in enumerate(num):
            result += int(val) * (10 ** (length - 1 - idx))
        print(result)
        return result

    def multiply(self, num1: str, num2: str) -> str:
        return str(self.getNumeric(num1) * self.getNumeric(num2))


print(Solution().multiply("123", "456"))
