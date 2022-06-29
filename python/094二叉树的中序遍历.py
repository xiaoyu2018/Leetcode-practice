from binarytree import *

def inorderTraversal(root: TreeNode) -> list:
    res=[]
    def _iot(r:TreeNode):

        if(r):
            _iot(r.left)
            res.append(r.val)
            _iot(r.right)
    
    _iot(root)
    return res

