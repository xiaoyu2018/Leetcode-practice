#include"mybitree.h"
#include<stack>
#include<vector>
#include<algorithm>

int getMinimumDifference(TreeNode *root)
{
    stack<TreeNode *> st;
    st.push(root);
    int res = 0x7fffffff;
    int pre = 0x7fffffff;
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
            res = min(abs(pre - crt->val), res);
            pre = crt->val;
            memo.push_back(crt);
        }
        if(crt->right)
            st.push(crt->right);
    }
    return res;
}