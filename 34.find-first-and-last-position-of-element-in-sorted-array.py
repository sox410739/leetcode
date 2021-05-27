#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findLow(nums: List[int], target: int) -> int:
            left = 0
            right = len(nums)-1
            while(left <= right):
                middle = (left+right)//2
                if(nums[middle] < target):
                    left = middle+1
                    continue
                if(nums[middle] >= target):
                    right = middle-1
                    continue
            return left

        start = findLow(nums, target)
        End = findLow(nums, target+1)-1
        print(start, End)
        if(start <= End):
            return [start, End]
        return [-1, -1]
# @lc code=end

