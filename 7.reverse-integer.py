#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        answer = 0
        if(x >= 0):
            temp = str(x)
            temp = temp[::-1]
            answer = int(temp)
        else:
            temp = str(-x)
            temp = temp[::-1]
            answer = -int(temp)
        
        if(answer >= pow(2, 31)-1 or answer < -pow(2, 31)):
            return 0
        return answer
# @lc code=end

