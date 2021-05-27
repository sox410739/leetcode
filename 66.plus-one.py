#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        carry = 0
        for i in range(-1, -len(digits)-1, -1):
            temp = digits[i] + carry
            carry = temp // 10
            digits[i] = temp %10
        
        if(carry == 1):
            digits.insert(0, 1)
        
        return digits
# @lc code=end

