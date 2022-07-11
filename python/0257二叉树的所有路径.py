from binarytree import TreeNode


def binaryTreePaths(root:TreeNode) -> list:
    res=[]
    st=[]
    
    def _preTraversal(root:TreeNode):
        
        if(root):
            st.append(root)
            if(not root.left and not root.right):
                res.append("->".join([str(i.val) for i in st]))

            _preTraversal(root.left)
            _preTraversal(root.right)

            st.pop()
    
    _preTraversal(root)
    return res
