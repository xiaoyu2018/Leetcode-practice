#include"mybitree.h"

TreeNode *insertIntoBST(TreeNode *root, int val)
{
    if(!root)
        return new TreeNode(val);

    TreeNode *temp = root;
    while (temp)
    {
        if (val > temp->val)
        {
            if (!temp->right)
            {
                temp->right = new TreeNode(val);
                break;
            }
            temp = temp->right;
        }

        // val不会与BST中节点相等
        else
        {
            if (!temp->left)
            {
                temp->left = new TreeNode(val);
                break;
            }
            temp = temp->left;
        }
    }
    return root;
}