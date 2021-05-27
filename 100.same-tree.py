#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        post = []
        def postorder(root: TreeNode):
            if(root == None):
                post.append(None)
                return
            postorder(root.left)
            postorder(root.right)
            post.append(root.val)
        
        postorder(p)
        temp = post
        post = []
        postorder(q)

        if(temp == post):
            return True
        return False
# @lc code=end

