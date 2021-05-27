#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        climb = [0, 1, 2]
        for i in range(3, n+1):
            climb.append(climb[i-1] + climb[i-2])

        return climb[n]
# @lc code=end

