#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        temp = s.split()

        if(len(temp) == 0):
            return 0
        return len(temp[-1])
# @lc code=end

