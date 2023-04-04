from binarytree import TreeNode,pre_create


# 递归
def maxDepth(root:TreeNode) -> int:
    if(not root):
        return 0
    
    return 1+max(maxDepth(root.left),maxDepth(root.right))
def maxDepth(root:TreeNode) -> int:
    
    depth=0
    
    # 前序遍历
    def _get_depth(root:TreeNode,level:int):
        # 闭包中访问外部变量关键字nonelocal
        nonlocal depth
        if(root):
            depth=level if level>depth else depth
            _get_depth(root.left,level+1)
            _get_depth(root.right,level+1)
    
    _get_depth(root,1)
    return depth

print(maxDepth(pre_create([1,2,3])))