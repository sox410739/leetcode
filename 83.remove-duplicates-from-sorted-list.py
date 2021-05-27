#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if(not head):
            return head

        regist = head.val
        point = head
        while(point.next):
            temp = point.next
            if(temp.val == regist):
                point.next = temp.next
                del temp
                continue
            if(temp.val != regist):
                regist = temp.val
                point = temp
                continue
        
        return head
# @lc code=end

