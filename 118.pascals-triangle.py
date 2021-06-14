#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer = []
        
        while(numRows > 0):
            numRows -= 1
            
            if(len(answer) == 0):
                answer.append([1])
                continue

            answer.insert(-1, answer[-1].copy())
            answer[-1].insert(0, 0)
            for i, num in enumerate(answer[-2]):
                answer[-1][i] += num
        
        return answer

# @lc code=end

