#include<vector>
#include"mybitree.h"

// 左闭右开
TreeNode* Traversal(vector<int> &nums,int left,int right)
{
    if(left>=right)
        return nullptr;

    int val = nums[left];
    int idx = left;
    for (int i = left + 1; i < right; ++i)
    {
        if(val<nums[i])
        {
            idx = i;
            val = nums[i];
        }
    }

    TreeNode *root = new TreeNode(val);

    root->left = Traversal(nums, left, idx);
    root->right = Traversal(nums, idx+1, right);
    return root;
}

TreeNode *constructMaximumBinaryTree(vector<int> &nums)
{
    return Traversal(nums, 0, nums.size());
}