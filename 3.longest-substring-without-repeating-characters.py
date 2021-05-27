#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestSubstring = []
        longest = 0
        for i in s:
            while(i in longestSubstring):
                longestSubstring.remove(longestSubstring[0])
            longestSubstring.append(i)
            longest = max(longest, len(longestSubstring))

        return longest
# @lc code=end

