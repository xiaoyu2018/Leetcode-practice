#include "mybitree.h"
#include <stack>
#include <vector>
#include <algorithm>

vector<int> findMode(TreeNode *root)
{
    stack<TreeNode *> st;
    st.push(root);
    int temp = 0xffffffff;
    vector<int> res;
    int count = 0;
    int max_count = 0;
    vector<TreeNode *> memo;
    while (!st.empty())
    {
        TreeNode *crt = st.top();

        if (crt->left && find(memo.begin(), memo.end(), crt->left) == memo.end())
        {
            st.push(crt->left);
            continue;
        }
        else
        {
            st.pop();
            if (temp != crt->val)
                count = 0;
            temp = crt->val;
            ++count;

            if (count == max_count)
                res.push_back(temp);

            if (count > max_count)
            {
                max_count = count;
                res.clear();
                res.push_back(temp);
            }

            memo.push_back(crt);
        }
        if (crt->right)
            st.push(crt->right);
    }
    return res;
}