#include"mybitree.h"

TreeNode *deleteNode(TreeNode *root, int key)
{
    TreeNode *pre=nullptr;
    TreeNode *res = root;
    bool is_left;
    while (root)
    {
        if(root->val==key)
        {

            if(!root->left&&!root->right)
            {
                if(!pre)
                    return nullptr;
                if (is_left)
                    pre->left = nullptr;
                else
                    pre->right = nullptr;
                
            }

            else if (!root->left)
            {
                if (!pre)
                    return root->right;
                if (is_left)
                    pre->left = root->right;
                else
                    pre->right = root->right;
            }

            else if (!root->right)
            {
                if (!pre)
                    return root->left;
                if (is_left)
                    pre->left = root->left;
                else
                    pre->right = root->left;
            }

            else
            {
                TreeNode *left = root->left;
                TreeNode *right = root->right;

                for (;right->left;right=right->left)
                    ;
                right->left = left;

                if (!pre)
                    return root->right;
                if (is_left)
                    pre->left = root->right;
                else
                    pre->right = root->right;
            }

            break;
        }

        pre = root;
        if(key<root->val)
        {
            is_left = true;
            root = root->left;
        }

        else
        {
            is_left = false;
            root = root->right;
        }
    }

    return root;
}