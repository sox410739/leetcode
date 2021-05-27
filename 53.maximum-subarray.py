#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentValue = nums[0]
        maxValue = nums[0]
        for i in range(1, len(nums)):
            currentValue = max(currentValue + nums[i], nums[i])
            maxValue = max(maxValue, currentValue)

        return maxValue
# @lc code=end

