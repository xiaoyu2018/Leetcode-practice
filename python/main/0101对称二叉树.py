from binarytree import TreeNode,level_create


# 当二叉树对称时显然有中左右=中右左
# 进一步可以对左子树中左右遍历，右子树中右左遍历比较是否相同
def isSymmetric1(root:TreeNode) -> bool:
    def _tlr(node:TreeNode):
        trav=[]
        st=[node]
        while(st):
            crt=st.pop()
            trav.append(crt.val if(crt!=None) else None)
            if(crt):
                st.append(crt.right)
                st.append(crt.left)
        return trav

    def _trl(node:TreeNode):
        trav=[]
        st=[node]
        while(st):
            crt=st.pop()
            trav.append(crt.val if(crt!=None) else None)
            if(crt):
                st.append(crt.left)
                st.append(crt.right)
        return trav

    
    tlr_trav=_tlr(root.left)
    trl_trav=_trl(root.right)

    if(tlr_trav!=trl_trav):
        return False

    return True

# 更进一步，中途发现不同时就可以提前退出
def isSymmetric2(root:TreeNode) -> bool:
    lq=[root.left]
    rq=[root.right]

    while(lq or rq):
        l_node=lq.pop()
        r_node=rq.pop()
        if(not (l_node or r_node)):
            continue
        
        elif(l_node and r_node):
            if(l_node.val!=r_node.val):
                return False
            if(l_node):
                lq.append(l_node.right)
                lq.append(l_node.left)
            if(r_node):
                rq.append(r_node.left)
                rq.append(r_node.right)
                
        else:
            return False
        
    return True

print(isSymmetric2(level_create([1])))