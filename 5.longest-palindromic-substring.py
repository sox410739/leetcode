#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if(len(s) <= 1 or s == s[::-1]):
            return s

        startIndex = 1
        maxLen = 1
        for i in range(1 ,len(s)):
          
            odd = s[i - maxLen - 1 : i + 1]
            even = s[i - maxLen : i + 1]
            if i - maxLen - 1 >= 0 and odd == odd[::-1]:
                startIndex = i - maxLen - 1
                maxLen += 2
            elif i - maxLen >= 0 and even == even[::-1]:
                startIndex = i - maxLen
                maxLen += 1
                
        return s[startIndex : startIndex + maxLen]

        # dpMatrix = []
        # length = len(s)
        # LPS = ''
        # for i in range(length):
        #     dpMatrix.insert(i, [])
        #     for j in range(length):
        #         dpMatrix[i].append(0)
        
        # for i in range(length):
        #     dpMatrix[i][i] = 1
        #     if(dpMatrix[i][i] > len(LPS)):
        #         LPS = s[i]
        #     for j in range(i):
        #         if(i-j == 1 and s[i] == s[j]):
        #             dpMatrix[j][i] = 2
        #             if(dpMatrix[j][i] > len(LPS)):
        #                 LPS = s[j:i+1]
        #             continue
        #         if(dpMatrix[j+1][i-1] > 0 and s[i] == s[j]):
        #             dpMatrix[j][i] = dpMatrix[j+1][i-1]+2
        #             if(dpMatrix[j][i] > len(LPS)):
        #                 LPS = s[j:i+1]
        #             continue
        

        # return LPS
# @lc code=end

