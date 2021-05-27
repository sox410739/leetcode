#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        countAndSayString = '1'
        for i in range(1, n):
            countList = []
            for j in countAndSayString:
                if(len(countList) == 0):
                    countList.append([j, 1])
                    continue
                if(j == countList[-1][0]):
                    countList[-1][1] += 1
                    continue
                if(j != countList[-1][0]):
                    countList.append([j, 1])
                    continue
            countAndSayString = ''
            for j in countList:
                countAndSayString += str(j[1])
                countAndSayString += j[0]
            print(countAndSayString)
        
        return countAndSayString
# @lc code=end

