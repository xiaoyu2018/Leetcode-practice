#include<vector>
#include"mybitree.h"
#include<deque>

vector<double> averageOfLevels(TreeNode *root)
{
    vector<double> res;
    deque<TreeNode *> nodes;

    nodes.push_back(root);

    while (!nodes.empty())
    {
        double s = 0;
        int count = 0;

        int size = nodes.size();

        for (int i = 0; i < size; ++i)
        {
            TreeNode *crt = nodes.front();
            nodes.pop_front();
            if (!crt)
                continue;
            
            ++count;
            s += crt->val;
            nodes.push_back(crt->left);
            nodes.push_back(crt->right);
        }
        if (count)
            res.push_back(s/count);
    }

    return res;
}