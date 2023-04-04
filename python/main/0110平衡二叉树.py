from binarytree import TreeNode



def isBalanced(root: TreeNode) -> bool:
    # 求子树高度，若高度相差大于一则直接返回-1（不为平衡二叉树）
    # 否则继续求出父树高度
    def _getHeight(root):
        if(not root):
            return 0
        lh=_getHeight(root.left)
        if(lh==-1):return -1    
        rh=_getHeight(root.right)
        if(rh==-1):return -1

        res=abs(lh-rh)
        return 1+max(lh,rh) if res<2 else -1

    return  not(_getHeight(root)==-1)
