#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count = 0

    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if(not root):
            return False
        answer = self.DFS(root, 0, targetSum)
        
        if(not answer):
            return False
        return True
    #[1, 2, 3] \n4
    def DFS(self, current, preSum, targetSum):
        self.count += 1
        nowSum = preSum + current.val
        if(nowSum == targetSum and not current.left and not current.right):
            return True
        
        if(current.left):
            temp = self.DFS(current.left, nowSum, targetSum)
            if(temp):
                return temp
        if(current.right):
            temp = self.DFS(current.right, nowSum, targetSum)
            if(temp):
                return temp
# @lc code=end

