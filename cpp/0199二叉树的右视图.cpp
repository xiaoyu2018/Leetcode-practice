#include <vector>
#include "mybitree.h"
#include <deque>

vector<int> levelOrder(TreeNode *root)
{
    vector<int> res;
    deque<TreeNode *> nodes;

    nodes.push_back(root);

    while (!nodes.empty())
    {
        int temp=101;

        int size = nodes.size();

        for (int i = 0; i < size; ++i)
        {
            TreeNode *crt = nodes.front();
            nodes.pop_front();
            if (!crt)
                continue;

            temp=crt->val;
            nodes.push_back(crt->left);
            nodes.push_back(crt->right);
        }
        if (temp!=101)
            res.push_back(temp);
    }

    return res;
}

int main()
{
}