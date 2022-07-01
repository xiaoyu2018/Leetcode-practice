#include<deque>
#include<iostream>
using namespace std;

struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;

    TreeNode() : val(0), left(nullptr), right(nullptr){} 
    TreeNode(int x) : val(x), left(nullptr), right(nullptr){} 
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};


TreeNode* Create(deque<int>& dq)
{
    if(dq.empty()||dq.front()==NULL)
    {
        dq.pop_front();
        return nullptr;
    }

    int val = dq.front();
    dq.pop_front();
    
    TreeNode *node = new TreeNode(val);
    node->left = Create(dq);
    node->right = Create(dq);

    return node;
}
