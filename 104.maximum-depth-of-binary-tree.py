#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def DFS(current: TreeNode, depth: int):
            if(not current):
                return depth
            
            depth += 1
            return max(DFS(current.left, depth), DFS(current.right, depth))

        return DFS(root, 0)
            
# @lc code=end

