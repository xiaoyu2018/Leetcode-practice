#include "mybitree.h"
#include <vector>
#include<stack>

// 递归
void Traversal(TreeNode *root, vector<int> &res)
{
    if (root)
    {
        Traversal(root->left, res);
        res.push_back(root->val);
        Traversal(root->right, res);
    }
}

void Traversal2(TreeNode *root, vector<int> &res)
{
    stack<TreeNode *> st;
    TreeNode *cur = root;
    while (cur != NULL || !st.empty())
    {
        if (cur != NULL)
        {                    // 指针来访问节点，访问到最底层
            st.push(cur);    // 将访问的节点放进栈
            cur = cur->left; // 左
        }
        else
        {
            cur = st.top(); // 从栈里弹出的数据，就是要处理的数据（放进result数组里的数据）
            st.pop();
            res.push_back(cur->val);    // 中
            cur = cur->right;           // 右
        }
    }
    
}

vector<int> inorderTraversal(TreeNode *root)
{
    vector<int> res;
    Traversal2(root, res);

    return res;
}


int main()
{
}