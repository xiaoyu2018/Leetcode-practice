from binarytree import TreeNode,level_create

def mergeTrees1(root1: TreeNode, root2: TreeNode) -> TreeNode:

    def _traversal(r1:TreeNode,r2:TreeNode,p:TreeNode,left=True):
        
        if(r1 and r2):
            r1.val+=r2.val
        
        # 如果遍历到r1中none节点，直接使其父节点指向r2对应节点，并返回本层递归
        elif(not r1 and r2):
            if(left):
                p.left=r2
            else:
                p.right=r2
            return
        
        # 遍历到r2中none时，直接返回
        else:return

        _traversal(r1.left,r2.left,r1)
        _traversal(r1.right,r2.right,r1,False)

    if(not root1):
        return root2
    
    _traversal(root1,root2,root1)

    return root1



def mergeTrees(root1: TreeNode, root2: TreeNode) -> TreeNode:
    if(not root1):
        return root2
    if(not root2):
        return root1
    
    root1.val+=root2.val

    root1.left=mergeTrees(root1.left,root2.left)
    root1.right=mergeTrees(root1.right,root2.right)

    return root1