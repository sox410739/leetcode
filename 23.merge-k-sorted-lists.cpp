/*
 * @lc app=leetcode id=23 lang=cpp
 *
 * [23] Merge k Sorted Lists
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
// #include <iostream>
// #include <vector>
// struct ListNode {
//     int val;
//     ListNode *next;
//     ListNode() : val(0), next(nullptr) {}
//     ListNode(int x) : val(x), next(nullptr) {}
//     ListNode(int x, ListNode *next) : val(x), next(next) {}
// };
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if(lists.empty()){
            return nullptr;
        }

        ListNode* answer = nullptr;

        for(int i=0;i<lists.size();i++){
            answer = mergeTwo(answer, lists[i]);
        }
        
        return answer;
    }
    #include <stdlib.h>

    ListNode* mergeTwo(ListNode* first, ListNode* second){
        ListNode* head = new ListNode(-1);
        ListNode* current = head;

        while(first && second){
            if(first->val <= second->val){
                current->next = first;
                first = first->next;
                current = current->next;
                continue;
            }
            if(first->val > second->val){
                current->next = second;
                second = second->next;
                current = current->next;
                continue;
            }
        }

        if(first){
            current->next = first;
        }
        if(second){
            current->next = second;
        }

        return head->next;
    }
};
// @lc code=end

