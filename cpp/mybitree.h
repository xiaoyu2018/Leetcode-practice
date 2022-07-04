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


TreeNode* PreCreate(deque<int>& dq)
{
    if(dq.empty()||dq.front()==NULL)
    {
        if(not dq.empty())
            dq.pop_front();
        return nullptr;
    }

    int val = dq.front();
    dq.pop_front();
    
    TreeNode *node = new TreeNode(val);
    node->left = PreCreate(dq);
    node->right = PreCreate(dq);

    return node;
}

TreeNode *LevelCreate(deque<int> &dq)
{
    deque<TreeNode *> nodes;
    if(dq.empty())
        return nullptr;

    TreeNode *root = new TreeNode(dq[0]);
    nodes.push_back(root);

    while(!dq.empty())
    {
        TreeNode *lc = dq.front() != NULL ? new TreeNode(dq.front()) : nullptr;
        dq.pop_front();
        if(dq.empty())
            break;
        TreeNode *rc = dq.front() != NULL ? new TreeNode(dq.front()) : nullptr;
        dq.pop_front();

        TreeNode *crt = nodes.front();
        nodes.pop_front();
        if (lc)
        {
            crt->left = lc;
            nodes.push_back(lc);
        }
        if (rc)
        {
            crt->right = rc;
            nodes.push_back(rc);
        }

    }

    return root;
}