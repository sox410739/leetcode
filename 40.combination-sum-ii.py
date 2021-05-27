#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        candidates.append(0)
        answer = []
        self.recursive(candidates, target, [], answer)
        return answer

    def recursive(self, nums, target, tempList, answer):
        if(target < 0):
            return
        if(target == 0):
            answer.append(tempList)
            return
        for i in range(len(nums)):
            if(nums[i] != nums[i-1] or len(nums) == 1):
                self.recursive(nums[i+1:], target-nums[i], tempList + [nums[i]], answer)
# @lc code=end

