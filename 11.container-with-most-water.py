#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        Max = -1
        left = 0
        right = len(height)-1

        for i in range(len(height)):
            temp = min(height[left], height[right])*(right-left)
            Max = max(Max, temp)
            if(height[left] >= height[right]):
                right -= 1
                continue
            if(height[left] <  height[right]):
                left += 1
                continue

        return Max
# @lc code=end

