#include <vector>
#include "mybitree.h"
#include <deque>
#include<algorithm>

vector<vector<int>> levelOrder(TreeNode *root)
{
    vector<vector<int>> res;
    deque<TreeNode *> nodes;

    nodes.push_back(root);

    while (!nodes.empty())
    {
        vector<int> temp;

        int size = nodes.size();

        for (int i = 0; i < size; ++i)
        {
            TreeNode *crt = nodes.front();
            nodes.pop_front();
            if (!crt)
                continue;

            temp.push_back(crt->val);
            nodes.push_back(crt->left);
            nodes.push_back(crt->right);
        }
        if (!temp.empty())
            res.push_back(temp);
    }
    reverse(res.begin(),res.end());
    return res;
}

int main()
{
}