#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if(not root):
            return []
        
        self.output = []
        self.inorder(root)
        
        return self.output

    def inorder(self, current):
        if(current.left):
            self.inorder(current.left)
        
        self.output.append(current.val)

        if(current.right):
            self.inorder(current.right)
# @lc code=end

