#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums):
        import itertools
        string = ''.join(str(n) for n in nums)
        print(string)
        return list(set(itertools.permutations(nums, len(nums))))

if __name__ == "__main__":
    temp = Solution()
    print(temp.permuteUnique([1, 1, 2]))


# @lc code=end

