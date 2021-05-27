#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        counter = 0
        point = head

        while(point):
            counter += 1
            point = point.next
        if(counter == n):
            return head.next
        point = head
        counter -= n
        for i in range(counter-1):
            point = point.next
        temp = point.next
        point.next = temp.next
        del temp

        return head
        
# @lc code=end

