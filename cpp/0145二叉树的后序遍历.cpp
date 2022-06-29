#include "mybitree.h"
#include <vector>

void Traversal(TreeNode *root, vector<int> &res)
{
    if (root)
    {
        Traversal(root->left, res);
        Traversal(root->right, res);
        res.push_back(root->val);
    }
}


vector<int> postorderTraversal(TreeNode *root)
{
    vector<int> res;
    Traversal(root, res);

    return res;
}
