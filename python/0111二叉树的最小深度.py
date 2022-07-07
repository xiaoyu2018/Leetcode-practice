from binarytree import TreeNode

# 最小深度是指根节点到叶子节点的的最短距离
# 不要与求最大深度的算法混淆
def minDepth(root: TreeNode) -> int:
    if(not root):
        return 0
    if(root.left and not root.right):
        return 1+minDepth(root.left)
    if(root.right and not root.left):
        return 1+minDepth(root.right)
    
    return 1+min(minDepth(root.left),minDepth(root.right))