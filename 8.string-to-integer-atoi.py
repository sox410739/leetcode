#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:

        temp = s.split()
        number = ''
        Max = pow(2, 31)  -1
        Min = -pow(2, 31)
        point = 0

        while(point < len(s)):
            if(s[point] == ' '):
                point += 1
                continue
            if(s[point] == '+' or s[point] == '-' or (s[point] >= '0' and s[point] <= '9')):
                number += s[point]
                for i in range(point+1, len(s)):
                    if(s[i] < '0' or s[i] > '9'):
                        break
                    number += s[i]
                break

            return 0
        print(number)

        try:
            int(number)
        except ValueError:
            return 0
        
        if(int(number) > Max):
            return Max
        if(int(number) < Min):
            return Min
        return int(number)
# @lc code=end

