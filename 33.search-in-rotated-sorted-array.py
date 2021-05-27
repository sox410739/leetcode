#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if(not target in nums):
            return -1
        
        return nums.index(target)
                
# @lc code=end

