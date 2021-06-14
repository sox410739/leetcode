/*
 * @lc app=leetcode id=25 lang=cpp
 *
 * [25] Reverse Nodes in k-Group
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
// struct ListNode {
//     int val;
//     ListNode *next;
//     ListNode() : val(0), next(nullptr) {}
//     ListNode(int x) : val(x), next(nullptr) {}
//     ListNode(int x, ListNode *next) : val(x), next(next) {}
// };

public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        int reverseNum = k;
        bool firstReverseFlag = true;
        ListNode* current = head;
        ListNode* re_head = head;
        ListNode* pre_re_head = (ListNode*)malloc(sizeof(ListNode));
        pre_re_head->next = head;

        while(current){
            k--;
            if(k == 0){
                Reverse(re_head, current->next);
                if(firstReverseFlag){
                    head = current;
                    firstReverseFlag = false;
                }
                pre_re_head->next = current;
                current = re_head;
                pre_re_head = re_head;
                re_head = re_head->next;
                k = reverseNum;
            }
            current = current->next;
        }

        return head;
    }

    void Reverse(ListNode* head, ListNode* tail_next){
        ListNode* current = head->next;
        ListNode* pre_current = head;
        pre_current->next = nullptr;

        while(current != tail_next){
            ListNode* temp = current->next;
            current->next = pre_current;
            pre_current = current;
            current = temp;
        }
        head->next = tail_next;
    }
};
// @lc code=end

