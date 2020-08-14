#include<bits/stdc++.h>
using namespace std;


//Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

//
// Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
// Output: 7 -> 0 -> 8
// Explanation: 342 + 465 = 807.

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* ans = new ListNode();
        vector<int> ansv;
        int c = 0;
        while(l1 && l2){
            int s = l1->val + l2->val + c;
            c = s /10;
            ansv.push_back(s%10);
            l1=l1->next;
            l2=l2->next;
        }
        while (l1 != NULL){
            int s = l1->val + c;
            c = s /10;
            ansv.push_back(s%10);
            l1=l1->next;
        }
        while (l2 != NULL){
            int s = l2->val + c;
            c = s /10;
            ansv.push_back(s%10);
            l2=l2->next;
        }
        if (c){
            ansv.push_back(c);
        }
        
        ListNode* temp = ans;
        
        for(int i = 0; i < ansv.size(); i++){
            temp -> val = ansv[i];
            if (i != ansv.size() - 1) {
                temp->next = new ListNode();
            }
            temp = temp->next;
        }
        
        return ans;
    }
};

int main(){
    return 0;
}