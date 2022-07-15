#include<vector>
#include"mybitree.h"

// 用下标记录位置，不真的切割数组
TreeNode *traversal(vector<int> &inorder, int inorderBegin, int inorderEnd, vector<int> &postorder, int postorderBegin, int postorderEnd)
{
    if (postorderBegin == postorderEnd)
        return NULL;

    int rootValue = postorder[postorderEnd - 1];
    TreeNode *root = new TreeNode(rootValue);

    if (postorderEnd - postorderBegin == 1)
        return root;

    int delimiterIndex;
    for (delimiterIndex = inorderBegin; delimiterIndex < inorderEnd; delimiterIndex++)
    {
        if (inorder[delimiterIndex] == rootValue)
            break;
    }
    // 切割中序数组
    // 左中序区间，左闭右开[leftInorderBegin, leftInorderEnd)
    int leftInorderBegin = inorderBegin;
    int leftInorderEnd = delimiterIndex;
    // 右中序区间，左闭右开[rightInorderBegin, rightInorderEnd)
    int rightInorderBegin = delimiterIndex + 1;
    int rightInorderEnd = inorderEnd;

    // 切割后序数组
    // 左后序区间，左闭右开[leftPostorderBegin, leftPostorderEnd)
    int leftPostorderBegin = postorderBegin;
    int leftPostorderEnd = postorderBegin + delimiterIndex - inorderBegin; // 终止位置是 需要加上 中序区间的大小size
    // 右后序区间，左闭右开[rightPostorderBegin, rightPostorderEnd)
    int rightPostorderBegin = postorderBegin + (delimiterIndex - inorderBegin);
    int rightPostorderEnd = postorderEnd - 1; // 排除最后一个元素，已经作为节点了

    root->left = traversal(inorder, leftInorderBegin, leftInorderEnd, postorder, leftPostorderBegin, leftPostorderEnd);
    root->right = traversal(inorder, rightInorderBegin, rightInorderEnd, postorder, rightPostorderBegin, rightPostorderEnd);

    return root;
}

TreeNode *buildTree(vector<int> &inorder, vector<int> &postorder)
{
    if (inorder.size() == 0 || postorder.size() == 0)
        return NULL;
    // 左闭右开的原则
    return traversal(inorder, 0, inorder.size(), postorder, 0, postorder.size());
}