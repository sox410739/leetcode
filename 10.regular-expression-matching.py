#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        import re
        regex = re.compile(p)
        match = regex.search(s)

        if(not match):
            return False
        return s == match.group(0)
# @lc code=end

