#include "mybitree.h"
#include <vector>
#include <stack>

// 递归
void Traversal(TreeNode *root, vector<int> &res)
{
    if (root)
    {
        Traversal(root->left, res);
        Traversal(root->right, res);
        res.push_back(root->val);
    }
}

void Traversal2(TreeNode *root, vector<int> &res)
{
    stack<TreeNode *> st;
    st.push(root);

    while(!st.empty())
    {
        if()
    }
}

vector<int> postorderTraversal(TreeNode *root)
{
    vector<int> res;
    if(root==nullptr)
        return res;
    Traversal2(root, res);

    return res;
}
