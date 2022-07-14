#include"mybitree.h"
#include<stack>
#include<utility>


bool hasPathSum(TreeNode *root, int targetSum)
{
    if(!root)
        return false;
    stack<pair<TreeNode *, int>> nodes;
    nodes.push(pair<TreeNode *, int>(root, root->val));

    while (!nodes.empty())
    {
        pair<TreeNode *, int> node = nodes.top();
        nodes.pop();
        if(!node.first->left&&!node.first->right&&node.second==targetSum)
            return true;
        
        if (node.first->left)
            nodes.push(pair<TreeNode *, int>(node.first->left, node.second + node.first->left->val));

        if (node.first->right)
            nodes.push(pair<TreeNode *, int>(node.first->right, node.second + node.first->right->val));
        
    }

    return false;
}