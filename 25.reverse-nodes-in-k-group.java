
/*
 * @lc app=leetcode id=25 lang=java
 *
 * [25] Reverse Nodes in k-Group
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    // public static class ListNode {
    //         int val;
    //         ListNode next;
    //         ListNode() {}
    //         ListNode(int val) { this.val = val; }
    //         ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    // }
    public ListNode reverseKGroup(ListNode head, int k) {
        ListNode current = head;
        ListNode re_head = head;
        int reverseNum = k;
        boolean firstReverseFlag = true;

        while(current != null){
            k--;
            if(k == 0){
                System.out.println("current.next:"  + current.next.val);
                reverse(re_head, current.next);
                if(firstReverseFlag){
                    head = current;
                    firstReverseFlag = false;
                }
                re_head = re_head.next;
                current = re_head;
                k = reverseNum-1;
            }
            printList(head);
            current = current.next;
        }

        return head;
    }

    public void reverse(ListNode head, ListNode tail_next){
        System.out.println("----------------");
        printList(head);
        System.out.println("----------------");
        ListNode current = head;
        ListNode pre_current = current;
        current = current.next;
        pre_current.next = null;

        while(!current.equals(tail_next)){
            ListNode temp = current.next;
            current.next = pre_current;
            pre_current = current;
            current = temp;
        }
        head.next = tail_next;
        System.out.println("hi");
    }

    public void printList(ListNode head){
        ListNode current = head;

        while(current != null){
            System.out.print(current.val);
            System.out.print(' ');
            current = current.next;
        }
        System.out.println();
    }
}
// @lc code=end

