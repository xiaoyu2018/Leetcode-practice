from binarytree import TreeNode,level_create

def getMinimumDifference(root: TreeNode) -> int:
    res=float("inf")
    pre=float("inf")
    def _traversal(root:TreeNode):
        nonlocal res
        nonlocal pre

        if(not root):
            return

        if(root.left):
            _traversal(root.left)
        
        res=min(abs(pre-root.val),res)
        pre=root.val

        if(root.right):
            _traversal(root.right)

    _traversal(root)

    return res


print(getMinimumDifference(level_create([236,104,701,None,227,None,911])))
