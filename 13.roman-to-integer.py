#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        table = dict()
        table['I'] = 1
        table['V'] = 5
        table['X'] = 10
        table['L'] = 50
        table['C'] = 100
        table['D'] = 500
        table['M'] = 1000

        number = 0
        for i in range(len(s)):
            number += table[s[i]]
            if((s[i] == 'V' or s[i] == 'X') and (i > 0 and s[i-1] == 'I')):
                number -= 2
                continue
            if((s[i] == 'L' or s[i] == 'C') and (i > 0 and s[i-1] == 'X')):
                number -=20
                continue
            if((s[i] == 'D' or s[i] == 'M') and (i > 0 and s[i-1] == 'C')):
                number -= 200
                continue

        return number
# @lc code=end

