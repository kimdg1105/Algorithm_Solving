class Solution:
    def myAtoi(self, s: str) -> int:
        ispositive = 1
        numstart = False
        ans = ""
        start = False

        for idx, c in enumerate(s):
            if c == " " and numstart == False:
                if start == True:
                    break
                continue

            if numstart == False and c == "-":
                if start == True:
                    break
                ispositive = -1
                start = True
                continue

            if numstart == False and c == "+":
                if start == True:
                    break
                start = True
                continue

            if c in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
                ans += c
                start = True
                numstart = True
                continue
            else:
                break

        if ans == "":
            return 0

        answer = int(ans) * ispositive

        if answer > pow(2, 31) - 1:
            answer = pow(2, 31) - 1
        elif answer < -pow(2, 31):
            answer = -pow(2, 31)

        return answer


print(Solution().myAtoi("  +  413"))
print(Solution().myAtoi("+-12"))
