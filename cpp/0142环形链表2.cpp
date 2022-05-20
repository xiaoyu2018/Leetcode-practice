#include<unordered_set>
#include"mylinklist.h"

using namespace std;

ListNode *detectCycle(ListNode *head)
{

    unordered_set<ListNode *> memo;

    while (head)
    {
        if(memo.find(head)!=memo.end())
            return head;
        memo.insert(head);
        head = head->next;
    }

    return NULL;
}

