from binarytree import TreeNode

def countNodes1(root: TreeNode) -> int:
    count=0

    def _preTraversal(root):
        nonlocal count
        if(root):
            count+=1
            _preTraversal(root.left)
            _preTraversal(root.right)
    
    _preTraversal(root)
    return count

def countNodes2(root:TreeNode)->int:
    if(not root):
        return 0
    return 1+countNodes2(root.left)+countNodes2(root.right)

# 利用完全二叉树性质
def countNodes(root:TreeNode)->int:
    if(not root):
        return 0
    
    leftdepth=rightdepth=0

    p=root.left
    while(p):
        leftdepth+=1
        p=p.left
    p=root.right
    while(p):
        leftdepth+=1
        p=p.right
    
    # 左右子树深度相同则为满二叉树
    if(leftdepth==rightdepth):
        return (2<<leftdepth)-1
    
    # 若不为满二叉树则继续检测左右子树是否分别为满二叉树
    return 1+countNodes(root.left)+countNodes(root.right)