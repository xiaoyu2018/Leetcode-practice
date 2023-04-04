from binarytree import TreeNode

def findBottomLeftValue(root:TreeNode) -> int:
    # 最大深度、最后一层最左叶子值
    lst=[1,root.val]

    def _traversal(root:TreeNode,depth:int=1):
        if(root):
            # 只记录同一层最先进入的节点的值
            if(depth>lst[0]):
                lst[1]=root.val
                lst[0]=depth
            # 先进入左子树
            _traversal(root.left,depth+1)
            _traversal(root.right,depth+1)
    
    _traversal(root)

    return lst[1]