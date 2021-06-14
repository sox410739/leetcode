#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        maxDis = []
        for i, n in enumerate(nums):
            maxDis.append(i+n)
        count = 0
        goal = len(nums)-1

        while(goal > 0):
            for i, n in enumerate(maxDis):
                if(n >= goal):
                    count += 1
                    goal = i
                    break
        return count

        
# @lc code=end

