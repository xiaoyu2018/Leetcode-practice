#include"mybitree.h"
#include<deque>

// 递归
TreeNode *invertTree(TreeNode *root)
{
    if(!root||(!root->left&&!root->right))
        return root;

    TreeNode *lc = invertTree(root->left);
    TreeNode *rc = invertTree(root->right);

    root->left = rc;
    root->right = lc;

    return root;
}

// 迭代
TreeNode* invertTree(TreeNode*root)
{
    deque<TreeNode *> nodes;
    nodes.push_back(root);

    while(!nodes.empty())
    {
        TreeNode *crt = nodes.front();
        nodes.pop_front();
        if(crt!=nullptr)
        {
            TreeNode *temp = crt->left;
            crt->left = crt->right;
            crt->right = temp;
            nodes.push_back(crt->left);
            nodes.push_back(crt->right);
        }

    }

    return root;
}