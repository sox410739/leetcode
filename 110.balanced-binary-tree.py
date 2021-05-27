#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if(root == None):
            return True
        
        if(abs(self.DFS(root.left)-self.DFS(root.right)) <= 1):
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        return False
    def DFS(self, root: TreeNode):
        if(root == None):
            return 0
        return 1 + max(self.DFS(root.left), self.DFS(root.right))
# @lc code=end

