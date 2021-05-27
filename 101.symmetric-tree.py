#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        leftList = []
        rightList = []
        def parseLeftTree(current: TreeNode):
            if(current.left):
                parseLeftTree(current.left)
            if(not current.left):
                leftList.append(None)
            if(current.right):
                parseLeftTree(current.right)
            if(not current.right):
                leftList.append(None)
            leftList.append(current.val)
        def parseRightTree(current: TreeNode):
            if(current.right):
                parseRightTree(current.right)
            if(not current.right):
                rightList.append(None)
            if(current.left):
                parseRightTree(current.left)
            if(not current.left):
                rightList.append(None)
            rightList.append(current.val)
        
        if(root.left):
            parseLeftTree(root.left)
        if(not root.left):
            leftList.append(None)
        if(root.right):
            parseRightTree(root.right)
        if(not root.right):
            rightList.append(None)
        
        print(leftList)
        print(rightList)
        return leftList == rightList
# @lc code=end

