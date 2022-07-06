#include<deque>
#include"mybitree.h"

// 迭代
int maxDepth(TreeNode *root)
{
    int res = 0;
    deque<TreeNode *> nodes;
    nodes.push_back(root);
    while(!nodes.empty())
    {
        bool exist_node = false;
        int size = nodes.size();
        for (int i = 0;i<size;++i)
        {
            TreeNode *crt = nodes.front();
            if (crt)
            {
                exist_node = true;
                nodes.push_back(crt->left);
                nodes.push_back(crt->right);
            }
            nodes.pop_front();
        }
        res += exist_node;
    }

    return res;
}