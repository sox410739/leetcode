#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()
        i = 0

        if(len(nums) < 3 or min(nums) > 0):
            return answer

        while(i <= len(nums)-3):
            j = i+1
            k = len(nums)-1
            while(j < k):
                temp = nums[i] + nums[j] + nums[k]
                if(temp == 0):
                    answer.insert(-1, [nums[i], nums[j], nums[k]])
                    try:
                        while(nums[j] == nums[j+1]):
                            j += 1
                        while(nums[k] == nums[k-1]):
                            k -= 1
                    except IndexError:
                        pass
                    j += 1
                    k -= 1
                    continue
                if(temp > 0):
                    k -= 1
                    continue
                if(temp < 0):
                    j += 1
                    continue
            try:
                while(nums[i] == nums[i+1]):
                    i += 1
            except IndexError:
                pass
            i += 1
        
        return answer
            
# @lc code=end

