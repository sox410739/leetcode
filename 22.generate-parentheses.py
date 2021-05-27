#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        def backtracking(string, left, right):
            if(len(string) == 2*n):
                answer.append(string)
                return
            if(left < n):
                backtracking(string+'(', left+1, right)
            if(left > right):
                backtracking(string+')', left, right+1)
        
        backtracking('', 0, 0)
        return answer
# @lc code=end

