#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    from itertools import permutations
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(permutations(nums))
# @lc code=end

