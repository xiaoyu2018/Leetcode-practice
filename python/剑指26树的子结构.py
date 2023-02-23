from binarytree import TreeNode

def isSubStructure(A: TreeNode, B: TreeNode) -> bool:
    if(A is None or B is None):
        return False

    def _is_sub(t1:TreeNode,t2:TreeNode):
        if(t2==None):
            return True
        
        if(t1==None or t1.val!=t2.val):
            return False
        
        return _is_sub(t1.left,t2.left) and _is_sub(t1.right,t2.right)

    def _dfs(root:TreeNode):
        
        if(root is None):
            return False
        if(_is_sub(root,B)):
            return True
        
        return _dfs(root.left) or _dfs(root.right)
    
    return _dfs(A)

