#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        answer = ''

        temp = num // 1000
        num %= 1000
        for i in range(temp):
            answer += 'M'
        
        temp = num // 100
        num %= 100
        if(temp == 9):
            answer += 'CM'
            temp = 0
        if(temp == 4):
            answer += 'CD'
            temp = 0
        if(temp >= 5):
            answer += 'D'
            temp -= 5
        for i in range(0, temp):
            answer += 'C'
        
        temp = num // 10
        num %= 10
        if(temp == 9):
            answer += 'XC'
            temp = 0
        if(temp == 4):
            answer += 'XL'
            temp = 0
        if(temp >= 5):
            answer += 'L'
            temp -= 5
        for i in range(0, temp):
            answer += 'X'

        temp = num
        if(temp == 9):
            answer += 'IX'
            temp = 0
        if(temp == 4):
            answer += 'IV'
            temp = 0
        if(temp >= 5):
            answer += 'V'
            temp -= 5
        for i in range(0, temp):
            answer += 'I'

        return answer

# @lc code=end

