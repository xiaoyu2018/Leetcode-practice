#include"mybitree.h"
#include<deque>

int minDepth(TreeNode *root)
{
    if(!root)
        return 0;
    int res = 0;
    deque<TreeNode *> nodes;
    nodes.push_back(root);

    while(!nodes.empty())
    {
        int size = nodes.size();
        ++res;
        for (int i = 0; i < size; ++i)
        {
            TreeNode *crt = nodes.front();
            nodes.pop_front();

            if(crt)
            {
                if(!crt->left&&!crt->right)
                    return res;
                nodes.push_back(crt->left);
                nodes.push_back(crt->right);
            }
        }
    }
    return res;
}