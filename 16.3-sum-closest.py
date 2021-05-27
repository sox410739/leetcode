#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = 100000
        i = 0

        while(i <= len(nums)-3):
            j = i+1
            k = len(nums)-1
            while(j < k):
                temp = nums[i] + nums[j] + nums[k]
                print(temp)
                if(abs(temp-target) < abs(closest-target)):
                    closest = temp
                if(temp > target):
                    k -= 1
                    continue
                if(temp <= target):
                    j += 1
                    continue
            i += 1

        return closest

# @lc code=end

