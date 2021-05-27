#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        answer = ListNode()
        front = answer
        front1 = l1
        front2 = l2
        while(front1 != None or front2 != None):
            answer.next = ListNode()
            answer = answer.next
            if(front1 == None):
                temp = carry + front2.val
                carry = temp//10
                answer.val = temp%10
                front2 = front2.next
                continue
            if(front2 == None):
                temp = carry + front1.val
                carry = temp//10
                answer.val = temp%10
                front1 = front1.next
                continue
            temp = carry + front1.val + front2.val
            carry = temp//10
            answer.val = temp%10
            front1 = front1.next
            front2 = front2.next

        if(carry > 0):
            answer.next = ListNode()
            answer = answer.next
            answer.val = carry
            carry = 0
        
        return front.next


# @lc code=end

