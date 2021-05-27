#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        self.recursive(candidates, target, [], answer)
        return answer

    def recursive(self, nums: List[int], target: int, tempList: List[int], answer: List[int]):
        if(target < 0):
            return
        if(target == 0):
            answer.append(tempList)
            return
        for i in range(len(nums)):
            self.recursive(nums[i:], target-nums[i], tempList+[nums[i]], answer)
# @lc code=end

