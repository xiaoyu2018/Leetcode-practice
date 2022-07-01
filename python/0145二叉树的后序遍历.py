from binarytree import *

def postorderTraversal1(root: TreeNode) -> list:
    res=[]
    def _iot(r:TreeNode):

        if(r):
            _iot(r.left)
            _iot(r.right)
            res.append(r.val)
    
    _iot(root)
    return res

def postorderTraversal2(root:TreeNode):
    res=[]

    if(not root):
        return res
    
    st=[root]
    memo=[None]

    while(st):
        top=st[-1]

        if(top.left in memo and top.right in memo):
            res.append(st.pop().val)
            memo.append(top)
        
        else:
            if(top.right):
                st.append(top.right)
            if(top.left):
                st.append(top.left)
        
        
    return res


print(postorderTraversal2(pre_create([1,None,2,3])))