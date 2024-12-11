class Solution:
    def longestPalindrome(self, s: str) -> int:
        strDict = {}
        for str in s:
            if str in strDict:
                strDict[str] += 1
            else:
                strDict[str] = 1

        ans = 0
        odd = 0
        for key in strDict:
            if strDict[key] % 2 == 1:
                ans += strDict[key] - 1
                odd = 1
            else:
                ans += strDict[key]

        return ans + odd


sol = Solution()
print(sol.longestPalindrome("asdfaa"))
