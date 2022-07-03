from binarytree import pre_create,TreeNode,level_create

# 递归
def preorderTraversal1(root: TreeNode) -> list:
    res=[]
    def _pot(r:TreeNode):
        
        if(r):
            res.append(r.val)
            _pot(r.left)
            _pot(r.right)
    
    _pot(root)
    
    return res

# 迭代
def preorderTraversal2(root: TreeNode):
    res=[]
    if(not root):
        return res
    
    st=[root]

    while(st):
        top=st.pop()
        res.append(top.val)

        if(top.right):
            st.append(top.right)
        if(top.left):
            st.append(top.left)
    
    return res


print(preorderTraversal2(level_create([1,2,3,4,5,6,7])))