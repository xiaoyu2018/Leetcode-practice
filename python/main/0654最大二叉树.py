from binarytree import TreeNode


def constructMaximumBinaryTree(nums:list) -> TreeNode:
    if(not nums):
        return None

    val=max(nums)
    idx=nums.index(val)
    root=TreeNode(val)

    root.left=constructMaximumBinaryTree(nums[:idx])
    root.right=constructMaximumBinaryTree(nums[idx+1:])

    return root
