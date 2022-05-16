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


ListNode *reverseList(ListNode *head)
{
    if(!head)
        return NULL;
    ListNode *prev = NULL;
    ListNode *cur = head;

    while(cur)
    {
        ListNode *temp = cur->next;
        cur->next = prev;
        prev = cur;
        cur = temp;
    }

    return prev;
}