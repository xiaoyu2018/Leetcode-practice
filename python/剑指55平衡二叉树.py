from binarytree import TreeNode

def isBalanced(root: TreeNode) -> bool:

    def _is_balanced(root:TreeNode):
        if(not root):
            return True,0
        l_b,l_v=_is_balanced(root.left)
        if(not l_b):
            return False,-1
        
        r_b,r_v=_is_balanced(root.right)
        if(not r_b):
            return False,-1

        if(abs(l_v-r_v)>1):
            return False,-1
        
        return True,1+max(l_v,r_v)

    return _is_balanced(root)[0]

        
        
