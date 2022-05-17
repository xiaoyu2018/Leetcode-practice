#include<vector>
#include<iostream>

struct ListNode
{
    int val;
    ListNode *next;
};

ListNode *Create(std::vector<int> nums)
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
        std::cout << head->val << " ";
    }
}