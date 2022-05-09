#include <iostream>
#include <vector>
using namespace std;

struct ListNode
{
    int val;
    ListNode *next;
};

ListNode *Create(vector<int> nums)
{
    if(!nums.size())
        return NULL;

    ListNode *head = new ListNode();
    ListNode *p = head;
    ListNode *q;
    p->val = nums[0];

    for (int i = 1;i<nums.size();++i)
    {
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

ListNode *deleteDuplicates(ListNode *head)
{
    if(!head)
        return head;
    ListNode *slow, *fast;
    slow = fast = head;

    while(fast)
    {
        if(slow->val!=fast->val)
        {
            slow->next = fast;
            slow = fast;
        }
        fast = fast->next;
    }
    slow->next = NULL;
    return head;
}

int main()
{
    vector<int> v = { 1,1,2};
    ListNode *head = Create(v);
    Show(deleteDuplicates(head));
}