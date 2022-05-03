#include <iostream>
#include <vector>
using namespace std;


struct ListNode
{
    int val;
    ListNode *next;
};

ListNode* Create(vector<int> nums)
{
    if(!nums.size())
        return NULL;
    ListNode *head=new ListNode();
    ListNode *p = head;
    ListNode *q;

    p->val = nums[0];
    for (int i = 1;i<nums.size();++i)
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

// 暴力
ListNode* MergeTwoList1(ListNode* list1, ListNode* list2)
{
    if (list1 == NULL)
        return list2;
    if (list2 == NULL)
        return list1;

    ListNode *res = new ListNode();
    ListNode *p = res;

    while(list1&&list2)
    {
        if(list1->val<list2->val)
        {
            p->next = list1;
            p = list1;
            list1 = list1->next;
        }
        else
        {
            p->next = list2;
            p = list2;
            list2 = list2->next;
        }

    }

    if(!list1)
        p->next = list2;
    if(!list2)
        p->next = list1;

    return res->next;
}

// 递归
ListNode* MergeTwoList2(ListNode* list1,ListNode* list2)
{
    if(list1==NULL)
        return list2;
    if(list2==NULL)
        return list1;

    if(list1->val<list2->val)
    {
        list1->next = MergeTwoList2(list1->next, list2);
        return list1;
    }
    else
    {
        list2->next = MergeTwoList2(list1, list2->next);
        return list2;
    }
}

int main()
{
    vector<int> v1 = {1, 2, 4};
    vector<int> v2 = {1, 3, 4};

    ListNode* l1 = Create(v1);
    ListNode* l2 = Create(v2);
    ListNode *l3 = MergeTwoList1(l1, l2);
    Show(l3);
}