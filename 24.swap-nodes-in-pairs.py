#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        newHead = ListNode(0, None)
        point = newHead
        while(head and head.next):
            point.next = ListNode(head.next.val, ListNode(head.val, None))
            point = point.next.next
            head = head.next.next
        if(head):
            point.next = head

        return newHead.next
# @lc code=end

