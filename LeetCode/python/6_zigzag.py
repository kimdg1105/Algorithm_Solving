class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        dict = {}
        for i in range(numRows):
            dict[i] = ""
        
        row = 0
        direction = 1
        for idx, char in enumerate(s):

            if direction:
                dict[row] = dict[row] + char
                row +=1    
            else :
                dict[row] = dict[row] + char
                row -=1

            if row == numRows :
                direction = 0
                row -=2
            if row == 0:
                direction = 1
                 

        ans = ""
        for key, value in dict.items():
            ans = ans + value
        
        return ans
    
print(Solution().convert("PAYPALISHIRING", 3))
