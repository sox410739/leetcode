#
# @lc app=leetcode id=6 lang=python3
#
# [6] ZigZag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if(numRows == 1):
            return s
            
        matrix = []
        for i in range(numRows):
            matrix.insert(i, [])
        
        point = 0
        reverseFlag = False
        for ch in s:
            matrix[point].append(ch)
            if(reverseFlag == True):
                point -= 1
                if(point == 0):
                    reverseFlag = False
                continue
            if(reverseFlag == False):
                point += 1
                if(point == numRows-1):
                    reverseFlag = True
                continue
        
        answer = ''
        for line in matrix:
            for ch in line:
                answer += ch
        
        return answer
# @lc code=end

