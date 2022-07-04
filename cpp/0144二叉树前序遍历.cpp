#include"mybitree.h"
#include<vector>
#include<stack>

// 递归
void Traversal1(TreeNode *root,vector<int>& res)
{
    if(root)
    {
        res.push_back(root->val);
        Traversal1(root->left, res);
        Traversal1(root->right, res);
    }
}

void Traversal2(TreeNode* root,vector<int>&res)
{
    stack<TreeNode*> st;
    TreeNode *temp;
    st.push(root);

    while(!st.empty())
    {
        temp = st.top();
        res.push_back(temp->val);
        st.pop();
        if (temp->right!=nullptr)
            st.push(temp->right);
        if(temp->left!=nullptr)
            st.push(temp->left);
    }

}

vector<int> preorderTraversal(TreeNode *root)
{
    vector<int> res;
    if(root==nullptr)
        return res;
    Traversal2(root, res);

    return res;
}

int main()
{
    deque<int> dq = {1,NULL, 2, 3};
    TreeNode *root = PreCreate(dq);

    vector<int> res = preorderTraversal(root);

    for(int i : res)
    {
        cout << i;
    }
}