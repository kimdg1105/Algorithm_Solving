class Solution:
    def doesAliceWin(self, s: str) -> bool:
        for v in s:
            if v in ["a", "e", "i", "o", "u"]:
                return True
        return False
