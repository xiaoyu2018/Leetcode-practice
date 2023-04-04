from binarytree import TreeNode

def hasPathSum(root: TreeNode, targetSum: int) -> bool:
    
    def _traversl(root:TreeNode,s=0):
        if(root):
            s+=root.val

            if(s==targetSum and not root.left and not root.right):
                return True
            
            return _traversl(root.left,s) or _traversl(root.right,s)
        
        return False
    return _traversl(root)

    