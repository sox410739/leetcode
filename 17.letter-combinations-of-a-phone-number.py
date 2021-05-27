#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if(digits == ''):
            return []

        letter = {'2':'abc',
                  '3':'def',
                  '4':'ghi',
                  '5':'jkl',
                  '6':'mno',
                  '7':'pqrs',
                  '8':'tuv',
                  '9':'wxyz'}
        answer = ['']

        for ch in digits:
            temp = []
            for i in answer:
                for j in letter[ch]:
                    temp.append(i+j)
            answer = temp
        
        return answer

# @lc code=end

