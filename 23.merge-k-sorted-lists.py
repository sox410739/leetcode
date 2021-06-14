#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists):
        if(len(lists) == 0):
            return None
        self.lists = lists

        while(len(lists) > 1):
            self.mergeTwo(self.lists[0], self.lists[1])
            print(self.lists)
            self.lists.remove(self.lists[1])

        return self.lists[0]


    def mergeTwo(self, first, second):
        first_pre = ListNode(-0.5, first)
        if(not first):
            self.lists[0] = self.lists[1]
            return

        while(first or second):
            if(not first):
                first_pre.next = second
                break
            if(not second):
                break

            if(first.val <= second.val):
                first = first.next
                first_pre = first_pre.next
                continue
            if(first.val > second.val):
                first_pre.next = ListNode(second.val, first)
                first_pre = first_pre.next
                second = second.next
                continue


def printList(L):
    while(L):
        print(L.val, end = ' ')
        L = L.next
    print()

if __name__ == "__main__":
    temp = Solution()
    # [1, 4, 5] [1, 3, 4]
    test = temp.mergeKLists([None, ListNode(1)])
    printList(test)
# @lc code=end

