#
# @lc app=leetcode id=49 lang=python
#
# [49] Group Anagrams
#

# @lc code=start
class Solution(object):
    def groupAnagrams(self, strs):
        answerDict = {}
        answer = []

        for s in strs:
            tempString = ''.join(sorted(s))
            if(tempString not in answerDict):
                answerDict[tempString] = []
            answerDict[tempString].append(s)
        
        for v in answerDict.values():
            answer.append(v)
        return answer
           

if __name__ == "__main__":
    test = {'1':10, '2':20, '3':30}

    print(test.values())
    print(test.keys())
    print(test.items())

# @lc code=end

