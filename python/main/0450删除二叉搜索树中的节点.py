from binarytree import TreeNode

def deleteNode(root: TreeNode, key: int) -> TreeNode:
    if(not root):
        return root
    
    if(root.val==key):

        if(not root.left and not root.right):
            return None
        
        if(not root.left):
            return root.right
        
        if(not root.right):
            return root.left
        
        left=root.left
        right=root.right

        while(right.left):
            right=right.left
        right.left=left
        return root.right
    
    if(key<root.val):
        root.left=deleteNode(root.left,key)
    else:
        root.right=deleteNode(root.right,key)

    return root