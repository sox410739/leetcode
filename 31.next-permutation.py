#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        goalNum = None
        for i in range(len(nums)-2, -1, -1):
            if(nums[i] < nums[i+1]):
                goalNum = i
                break
        if(goalNum == None):
            nums.reverse()
        if(goalNum != None):
            for i in range(len(nums)-1, -1, -1):
                if(nums[i] > nums[goalNum]):
                    temp = nums[i]
                    nums[i] = nums[goalNum]
                    nums[goalNum] = temp
                    nums[goalNum+1:] = nums[goalNum+1:][::-1]
                    break
# @lc code=end

