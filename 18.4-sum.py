#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        answer = []

        for i in range(len(nums)-3):
            for j in range(i+1, len(nums)-2):
                k = j+1
                l = len(nums)-1
                while(k < l):
                    temp = nums[i]+nums[j]+nums[k]+nums[l]
                    if(temp == target):
                        temp = [nums[i], nums[j], nums[k], nums[l]]
                        if(not temp in answer):
                            answer.insert(-1, temp)
                        try:
                            k += 1
                            l -= 1
                        except IndexError:
                            pass
                        continue
                    if(temp > target):
                        l -= 1
                        continue
                    if(temp < target):
                        k += 1
                        continue
            
        return answer
# @lc code=end

