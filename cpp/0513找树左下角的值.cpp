#include"mybitree.h"
#include<queue>

int findBottomLeftValue(TreeNode *root)
{   
    int res;
    queue<TreeNode *> nodes;
    nodes.push(root);

    while(!nodes.empty())
    {
        int size = nodes.size();

        for (int i = 0;i<size;++i)
        {
            TreeNode *crt = nodes.front();
            nodes.pop();
            if (i == 0)
                res = crt->val;
            
            if(crt->left)
                nodes.push(crt->left);
            if(crt->right)
                nodes.push(crt->right);
        }
    }

    return res;
}