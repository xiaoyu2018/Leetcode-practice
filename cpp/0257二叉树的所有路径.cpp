#include<vector>
#include<deque>
#include <stack>
#include<iostream>
#include"mybitree.h"

vector<string> binaryTreePaths(TreeNode *root)
{
    stack<TreeNode *> treeSt; 
    stack<string> pathSt;     
    vector<string> res;    
    if (root == NULL)
        return res;
    treeSt.push(root);
    pathSt.push(to_string(root->val));
    while (!treeSt.empty())
    {
        TreeNode *crt = treeSt.top();
        treeSt.pop(); 
        // 根到crt的路径
        string path = pathSt.top();
        pathSt.pop(); 
        
        if (crt->left == NULL && crt->right == NULL)
        { // 若crt是叶子节点，则记录根到crt路径到res
            res.push_back(path);
        }
        // 记录根到crt左右孩子的完整路径
        if (crt->right)
        { 
            treeSt.push(crt->right);
            pathSt.push(path + "->" + to_string(crt->right->val));
        }
        if (crt->left)
        { 
            treeSt.push(crt->left);
            pathSt.push(path + "->" + to_string(crt->left->val));
        }
    }
    return res;
}

int main()
{
    deque<int> nodes = {1, 2, NULL, 5, NULL,NULL,3};
    TreeNode *root = PreCreate(nodes);

    binaryTreePaths(root);
}