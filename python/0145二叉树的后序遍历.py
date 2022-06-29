from binarytree import *

def inorderTraversal(root: TreeNode) -> list:
    res=[]
    def _iot(r:TreeNode):

        if(r):
            _iot(r.left)
            _iot(r.right)
            res.append(r.val)
    
    _iot(root)
    return res

