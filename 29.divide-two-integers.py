#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        def smallDivine(a, b):
            counter = 0
            while(a >= b):
                a -= b
                counter += 1
            return str(counter), str(a)

        negaFlag = False
        if(dividend < 0):
            dividend = -dividend
            negaFlag = not negaFlag
        if(divisor < 0):
            divisor = -divisor
            negaFlag = not negaFlag
        dividend = str(dividend)
        divisor = str(divisor)
        temp = dividend[:len(divisor)-1]
        quotient = ''

        for i in range(len(divisor)-1, len(dividend)):
            temp = temp + dividend[i]
            quotientTemp, temp = smallDivine(int(temp), int(divisor))
            quotient += quotientTemp
        
        if(quotient == ''):
            quotient = '0'
        quotient = int(quotient)
        if(negaFlag):
            quotient = -quotient
        
        if(quotient < -pow(2, 31)):
            return -pow(2, 31)
        if(quotient > pow(2, 31)-1):
            return pow(2, 31)-1
        return quotient


# @lc code=end

