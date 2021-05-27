#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        current = ListNode()
        front = current
        while(l1 != None or l2 != None):
            current.next = ListNode()
            current = current.next
            if(l1 == None):
                current.val = l2.val
                l2 = l2.next
                continue
            if(l2 == None):
                current.val = l1.val
                l1 = l1.next
                continue
            if(l1.val <= l2.val):
                current.val = l1.val
                l1 = l1.next
                continue
            if(l1.val > l2.val):
                current.val = l2.val
                l2 = l2.next
                continue
        
        return front.next
                
# @lc code=end

