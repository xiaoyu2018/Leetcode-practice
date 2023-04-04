from binarytree import TreeNode

def mirrorTree(root: TreeNode) -> TreeNode:
    if(not root):
        return None
    
    if(root.left):
        mirrorTree(root.left)
    if(root.right):
        mirrorTree(root.right)
    
    root.left,root.right=root.right,root.left
    return root