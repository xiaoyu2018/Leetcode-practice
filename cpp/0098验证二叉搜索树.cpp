#include"mybitree.h"
#include<stack>
#include<vector>
#include<algorithm>

bool isValidBST(TreeNode *root)
{
    stack<TreeNode *> nodes;
    nodes.push(root);
    vector<TreeNode *> memo;
    TreeNode *pre = nullptr;

    while (!nodes.empty())
    {
        TreeNode *crt = nodes.top();

        if(crt->left && (find(memo.begin(),memo.end(),crt->left)==memo.end()))
            nodes.push(crt->left);
        
        else
        {
            nodes.pop();
            memo.push_back(crt);
            if (pre == nullptr || pre->val < crt->val)
                pre = crt;
            else
                return false;
            if(crt->right)
                nodes.push(crt->right);
        }

    }

    return true;
}