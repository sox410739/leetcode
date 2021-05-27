#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if(ch == '('):
                stack.append(1)
                continue
            if(ch == '['):
                stack.append(2)
                continue
            if(ch == '{'):
                stack.append(3)
                continue
            if(len(stack) == 0):
                return False
                continue
            if(ch == ')'):
                temp = stack.pop()
                if(temp != 1):
                    return False
                continue
            if(ch == ']'):
                temp = stack.pop()
                if(temp != 2):
                    return False
                continue
            if(ch == '}'):
                temp = stack.pop()
                if(temp != 3):
                    return False
                continue
        
        if(len(stack) > 0):
            return False
        return True
# @lc code=end

