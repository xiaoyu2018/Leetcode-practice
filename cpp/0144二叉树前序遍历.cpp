#include"mybitree.h"
#include<vector>

void Traversal(TreeNode *root,vector<int>& res)
{
    if(root)
    {
        res.push_back(root->val);
        Traversal(root->left, res);
        Traversal(root->right, res);
    }
}

vector<int> preorderTraversal(TreeNode *root)
{
    vector<int> res;
    Traversal(root, res);

    return res;
}

int main()
{

}