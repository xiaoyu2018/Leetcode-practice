#include<vector>
#include<iostream>

using namespace std;

struct ListNode
{
    int val;
    ListNode *next;
};

ListNode *Create(vector<int> nums)
{
    if (!nums.size())
        return NULL;
    ListNode *head = new ListNode();
    ListNode *p = head;
    ListNode *q;

    p->val = nums[0];
    for (int i = 1; i < nums.size(); ++i)
    {
        ListNode *q;
        q = new ListNode();
        q->val = nums[i];
        p->next = q;
        p = q;
    }
    p->next = NULL;
    return head;
}

void Show(ListNode *head)
{
    for (; head != NULL; head = head->next)
    {
        cout << head->val << " ";
    }
}

ListNode* swapPairs(ListNode* head)
{
    if(!head || !head->next)
        return head;

    ListNode *p1 = head;
    ListNode *p2 = head->next;
    p1->next = swapPairs(p2->next);
    p2->next = p1;

    return p2;
}