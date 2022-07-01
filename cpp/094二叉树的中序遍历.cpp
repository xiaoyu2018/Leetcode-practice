#include "mybitree.h"
#include <vector>

// 递归
void Traversal(TreeNode *root, vector<int> &res)
{
    if (root)
    {
        Traversal(root->left, res);
        res.push_back(root->val);
        Traversal(root->right, res);
    }
}

vector<int> inorderTraversal(TreeNode *root)
{
    vector<int> res;
    Traversal(root, res);

    return res;
}

int main()
{
}