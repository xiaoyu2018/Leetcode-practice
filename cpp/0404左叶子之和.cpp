#include<stack>
#include"mybitree.h"


int sumOfLeftLeaves(TreeNode *root)
{
    if(!root)
        return 0;
    int res = 0;

    stack<TreeNode *> nodes;
    nodes.push(root);

    while(!nodes.empty())
    {
        TreeNode *crt = nodes.top();
        nodes.pop();

        if(crt->left)
        {
            if(!crt->left->left&&!crt->left->right)
                res += crt->left->val;
            nodes.push(crt->left);
        }

        if(crt->right)
            nodes.push(crt->right);
    }

    return res;
}