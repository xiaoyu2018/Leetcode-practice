#include "mybitree.h"
#include <vector>
#include <stack>
#include<algorithm>


// 递归
void Traversal(TreeNode *root, vector<int> &res)
{
    if (root)
    {
        Traversal(root->left, res);
        Traversal(root->right, res);
        res.push_back(root->val);
    }
}

// 前序遍历是：中左右，只需调换顺序变成中右左，然后反转res即可变为后序的左右中
void Traversal2(TreeNode *root, vector<int> &res)
{
    stack<TreeNode *> st;
    st.push(root);

    while(!st.empty())
    {
        TreeNode *top = st.top();
        res.push_back(top->val);
        st.pop();

        if(top->left)
            st.push(top->left);
        if(top->right)
            st.push(top->right);
    }


}

vector<int> postorderTraversal(TreeNode *root)
{
    vector<int> res;
    if(root==nullptr)
        return res;
    Traversal2(root, res);

    reverse(res.begin(), res.end());
    return res;
}
