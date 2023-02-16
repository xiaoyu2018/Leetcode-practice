from binarytree import TreeNode

def pathSum(root: TreeNode, target: int) -> list:
    res=[]
    path=[]

    def _dfs(root:TreeNode):
        nonlocal target
        if(root):
            path.append(root.val)
            if(not root.left and not root.right and sum(path)==target):
                res.append(path.copy())
            _dfs(root.left)
            _dfs(root.right)
            path.pop()
    
    _dfs(root)
    return res