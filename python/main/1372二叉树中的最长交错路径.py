from binarytree import TreeNode

def longestZigZag(root: TreeNode) -> int:

    res=0
    def _solve(root:TreeNode,dir_left:bool,length:int):
        nonlocal res
        if(root==None):
            return

        res=max(res,length)    
        if(dir_left):
            _solve(root.left,False,length+1)
            _solve(root.right,True,1)
        else:
            _solve(root.right,True,length+1)
            _solve(root.left,False,1)
    
    _solve(root,True,0)
    return res
