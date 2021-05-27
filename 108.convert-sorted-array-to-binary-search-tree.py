#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def buildTree(root: TreeNode, Range: range):
            print(Range)
            if(len(Range) == 0):
                return

            middle = (Range[0] + Range[-1]+1)//2
            root.val = nums[middle]
            if(middle != Range[0]):
                root.left = TreeNode()
                buildTree(root.left, range(Range[0], middle))
            if(middle != Range[-1]):
                root.right = TreeNode()
                buildTree(root.right, range(middle+1, Range[-1]+1))
            
        root = TreeNode()
        buildTree(root, range(len(nums)))

        return root
            
# @lc code=end

