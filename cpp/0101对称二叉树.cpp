#include"mybitree.h"

// 递归判断对称位置节点val是否相等
bool Compare(TreeNode*lc,TreeNode*rc)
{
    if (lc == nullptr && rc == nullptr)
        return true;
    else if (lc != nullptr && rc != nullptr)
    {
        if(lc->val!=rc->val)
            return false;
        // 本层节点val相等，则继续判断子节点val是否对应相等
        bool b1 = Compare(lc->left, rc->right);
        bool b2 = Compare(rc->left, lc->right);

        return b1 && b2;
    }
    else
        return false;
}

bool isSymmetric(TreeNode *root)
{
    return Compare(root->left, root->right);
}