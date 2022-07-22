from binarytree import TreeNode

def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

    if(root in [None,p,q]):
        return root
    
    left=lowestCommonAncestor(root.left,p,q)
    right=lowestCommonAncestor(root.right,p,q)

    if(left and right):
        return root
    
    if(left):
        return left
    if(right):
        return right
    
    return None
    
    