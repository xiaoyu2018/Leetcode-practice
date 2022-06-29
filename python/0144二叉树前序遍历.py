from binarytree import pre_create,TreeNode

def preorderTraversal(root: TreeNode) -> list:
    res=[]
    def _pot(r:TreeNode):
        
        if(r):
            res.append(r.val)
            _pot(r.left)
            _pot(r.right)
    
    _pot(root)
    
    return res


print(preorderTraversal(pre_create([1,None,2,3])))