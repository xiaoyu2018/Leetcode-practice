#include<deque>
#include"mybitree.h"

int countNodes(TreeNode *root)
{
    if(!root)
        return 0;
    deque<TreeNode *> nodes;
    nodes.push_back(root);
    int res = 0;

    while(!nodes.empty())
    {
        int size = nodes.size();
        
        for (int i = 0; i < size; ++i)
        {
            TreeNode *crt = nodes.front();
            nodes.pop_front();

            if(crt)
            {
                ++res;
                nodes.push_back(crt->left);
                nodes.push_back(crt->right);
            }
        }
    }

    return res;
}