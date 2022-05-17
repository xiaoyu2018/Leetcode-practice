#include"mylinklist.h"

using namespace std;


ListNode* removeNthFromEnd(ListNode*head,int n)
{
    ListNode *extra_head = new ListNode();
    extra_head->next = head;
    ListNode *slow = extra_head;
    ListNode *fast = head;
    
    while(n-->0)
        fast = fast->next;
    
    while(fast)
    {
        fast = fast->next;
        slow = slow->next;

    }
    slow->next = slow->next->next;
    return extra_head->next;
}

int main()
{
    vector<int> v = {1, 2, 3};

    Show(Create(v));
}