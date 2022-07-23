from binarytree import TreeNode

def insertIntoBST(root: TreeNode, val: int) -> TreeNode:
    if(not root):
        return TreeNode(val)
    
    if(val>root.val):
        root.right=insertIntoBST(root.right,val)
    
    else:
        root.left=insertIntoBST(root.left,val)
    
    return root