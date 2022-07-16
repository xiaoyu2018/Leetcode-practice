from binarytree import TreeNode

def searchBST(root: TreeNode, val: int) -> TreeNode:
    if(not root):
        return None
    if(root.val==val):
        return root

    if(root.val>val):
        return searchBST(root.left,val)
    else:
        return searchBST(root.right,val)
