from binarytree import TreeNode,level_create

def sumOfLeftLeaves(root:TreeNode) -> int:
    count=0

    def _traversal(root:TreeNode,left=False):
        nonlocal count

        if(not root.left and not root.right and left):
            count+=root.val
        if(root.left):
            _traversal(root.left,True)
        if(root.right):
            _traversal(root.right)
        
    if(not root):
        return count
    
    _traversal(root)

    return count

def sumOfLeftLeaves(root:TreeNode) -> int:
    if(not root):
        return 0
    l_val=sumOfLeftLeaves(root.left)
    r_val=sumOfLeftLeaves(root.right)

    t_val=0
    if(root.left and not root.left.left and not root.left.right):
        t_val=root.left.val 
    
    return t_val+l_val+r_val
    

print(sumOfLeftLeaves(level_create([3,9,20,None,None,15,7])))