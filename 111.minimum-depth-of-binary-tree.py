#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if(not root):
            return 0
            
        BFSQueue = [root]
        depthQueue = [1]
        while(len(depthQueue) > 0):
            front = BFSQueue[0]
            frontDepth = depthQueue[0]
            if(not front.left and not front.right):
                break
            if(front.left):
                BFSQueue.append(front.left)
                depthQueue.append(frontDepth+1)
            if(front.right):
                BFSQueue.append(front.right)
                depthQueue.append(frontDepth+1)
            BFSQueue.remove(front)
            depthQueue.remove(frontDepth)

        return depthQueue[0]
# @lc code=end

