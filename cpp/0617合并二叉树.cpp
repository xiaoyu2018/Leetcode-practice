#include"mybitree.h"
#include<queue>

// 与python中第一个递归思路一样
TreeNode *mergeTrees(TreeNode *root1, TreeNode *root2)
{
    if(!root1)
        return root2;
    if(!root2)
        return root1;

    queue<TreeNode *> q1;
    queue<TreeNode *> q2;
    q1.push(root1);
    q2.push(root2);


    while(!q1.empty() and !q2.empty())
    {
        TreeNode *r1 = q1.front();
        q1.pop();
        TreeNode *r2 = q2.front();
        q2.pop();

        r1->val += r2->val;
        
        if(r1->left&&r2->left)
        {
            q1.push(r1->left);
            q2.push(r2->left);
        }
        if(r1->right&&r2->right)
        {
            q1.push(r1->right);
            q2.push(r2->right);
        }

        if(!r1->left&&r2->left)
            r1->left = r2->left;
        if(!r1->right&&r2->right)
            r1->right = r2->right;
        
    }

    return root1;
}