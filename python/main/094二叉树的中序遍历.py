from binarytree import *

def inorderTraversal1(root: TreeNode) -> list:
    res=[]
    if(not root):
        return res
    def _iot(r:TreeNode):

        if(r):
            _iot(r.left)
            res.append(r.val)
            _iot(r.right)
    
    _iot(root)
    return res



def inorderTraversal2(root: TreeNode) -> list:
    res=[]
    
    if(not root):
        return res
    
    st=[]
    p=root

    while(st or p):
        
        if(p):
            st.append(p)
            p=p.left
        
        else:
            p=st[-1]
            st.pop()
            res.append(p.val)
            p=p.right
        
    return res

print(inorderTraversal2(pre_create([1,None,2,3])))