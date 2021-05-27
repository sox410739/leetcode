#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if(strs == []):
            return ''
        
        answer = strs[0]
        for string in strs:
            temp = ''
            for i in range(len(string)):
                if(i == len(answer)):
                    break
                if(answer[i] == string[i]):
                    temp += answer[i]
                    continue
                if(answer[i] != string[i]):
                    break
            answer = temp
        
        return temp
# @lc code=end

